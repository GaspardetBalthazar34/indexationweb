from queue import PriorityQueue, Empty
import time
import logging
import json
from bs4 import BeautifulSoup
from threading import Thread, Lock
from urllib import robotparser, parse, error
from urllib.parse import urlparse
from utils.pagedownloader import fetch_page_content


class WebCrawler:
    def __init__(self, base_url, max_pages=50, num_threads=3, delay_seconds=2, max_links_per_page=15):
        self.base_url = base_url
        self.base_domain = urlparse(base_url).netloc
        self.max_pages = max_pages
        self.visited_pages = {}  # Dictionnaire {URL: timestamp}
        self.pending_pages = PriorityQueue()  # URLs à explorer (priorisées)
        self.pending_pages.put((0, base_url))  # Ajoute l'URL de départ avec priorité haute
        self.num_threads = num_threads
        self.delay_seconds = delay_seconds
        self.robots_parsers = {}
        self.extracted_data = []  # Liste des données extraites
        self.lock = Lock()
        self.crawling_active = True

        logging.info(f"WebCrawler initialisé avec {base_url}, max {max_pages} pages.")

    def is_allowed_by_robots(self, url):
        """Vérifie si l'URL peut être explorée selon robots.txt"""
        robots_url = parse.urljoin(url, "/robots.txt")
        if robots_url in self.robots_parsers:
            robots_parser = self.robots_parsers[robots_url]
        else:
            robots_parser = robotparser.RobotFileParser()
            robots_parser.set_url(robots_url)
            try:
                robots_parser.read()
                self.robots_parsers[robots_url] = robots_parser
            except error.URLError:
                logging.warning(f"Impossible d'accéder à {robots_url}, autorisation supposée.")
                return True  # Si robots.txt est inaccessible, on suppose que c'est autorisé.

        return robots_parser.can_fetch("*", url)

    def is_internal_url(self, url):
        """Vérifie si l'URL appartient au même domaine que l'URL de base"""
        url_domain = urlparse(url).netloc
        return url_domain == self.base_domain

    def extract_page_details(self, url, html_content):
        """Analyse une page HTML et extrait le titre, le premier paragraphe et les liens"""
        soup = BeautifulSoup(html_content, 'html.parser')

        title = soup.title.string.strip() if soup.title else "Titre inconnu"
        first_paragraph = soup.find('p').text.strip() if soup.find('p') else "Aucun paragraphe trouvé"

        extracted_links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            absolute_link = parse.urljoin(url, href)

            if self.is_internal_url(absolute_link):
                extracted_links.append({"url": absolute_link, "source_url": url})

        return {
            "url": url,
            "title": title,
            "first_paragraph": first_paragraph,
            "links": extracted_links
        }

    def add_url_to_queue(self, url):
        """Ajoute une URL à la file d'attente si elle n'a pas déjà été visitée ou en attente"""
        with self.lock:
            if (url not in self.visited_pages and
                self.is_internal_url(url) and
                len(self.visited_pages) < self.max_pages and
                url not in [item[1] for item in self.pending_pages.queue]):  # Évite les doublons

                priority = 0 if 'product' in url else 1
                self.pending_pages.put((priority, url))

    def process_page(self):
        """Télécharge et analyse une page web"""
        while self.crawling_active:
            try:
                priority, current_url = self.pending_pages.get(timeout=5)  # Attend 5 sec max pour éviter de bloquer
            except Empty:
                continue

            with self.lock:
                if len(self.visited_pages) >= self.max_pages:
                    self.crawling_active = False
                    break
                if current_url in self.visited_pages:
                    continue

                # Marquer l'URL comme visitée immédiatement pour éviter les doublons
                self.visited_pages[current_url] = time.time()

            logging.info(f"Traitement de {current_url}")

            # Vérifier si l'URL est autorisée par robots.txt
            if not self.is_allowed_by_robots(current_url):
                logging.info(f"Accès interdit par robots.txt : {current_url}")
                continue

            # Télécharger et analyser la page
            html_content = fetch_page_content(current_url)
            if html_content:
                page_data = self.extract_page_details(current_url, html_content)
                self.extracted_data.append(page_data)

                # Ajouter de nouvelles URLs à la file d'attente
                for link in page_data["links"]:
                    self.add_url_to_queue(link["url"])

            # Respecter la politesse en ajoutant un délai entre les requêtes
            time.sleep(self.delay_seconds)

    def start_crawling(self):
        """Démarre le crawling multi-threadé"""
        threads = []
        for i in range(self.num_threads):
            thread = Thread(target=self.process_page, name=f"Thread-{i+1}")
            thread.start()
            threads.append(thread)

        while any(t.is_alive() for t in threads):
            time.sleep(1)
            with self.lock:
                if len(self.visited_pages) >= self.max_pages:
                    self.crawling_active = False
                    break

        for thread in threads:
            thread.join()

    def save_results_to_json(self, output_file):
        """Sauvegarde les données extraites dans un fichier JSON"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.extracted_data, f, indent=4, ensure_ascii=False)
        logging.info(f"Données sauvegardées dans {output_file}.")
