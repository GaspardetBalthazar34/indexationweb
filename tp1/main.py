import argparse
import logging
import os
from webcrawler import WebCrawler
from utils.validurl import is_valid_url
from utils.filenamesanitizer import generate_sanitized_filename

# Configuration des arguments en ligne de commande
parser = argparse.ArgumentParser(description="Web Crawler")
parser.add_argument("-m", "--max_urls", type=int, default=50, help="Nombre maximum de pages à explorer")
parser.add_argument("-b", "--base_url", type=str, default="https://web-scraping.dev/products", help="URL de départ")
parser.add_argument("-o", "--output_path", type=str, help="Fichier de sortie JSON (généré automatiquement si non fourni)")
parser.add_argument("-t", "--num_threads", type=int, default=5, help="Nombre de threads utilisés")
parser.add_argument("-p", "--politeness_delay", type=int, default=5, help="Délai entre les requêtes")
args = parser.parse_args()

# Validation de l'URL de départ
if not is_valid_url(args.base_url):
    logging.error(f"URL invalide ou inaccessible : {args.base_url}")
    exit(1)

# Génération du nom du fichier de sortie si non fourni
if args.output_path is None:
    sanitized_name = generate_sanitized_filename(args.base_url)
    args.output_path = f"output/crawled_data_{sanitized_name}.json"

# Création du répertoire de sortie si nécessaire
os.makedirs(os.path.dirname(args.output_path), exist_ok=True)

# Configuration des logs
log_file = "output/logs.log"
open(log_file, "w").close()  # Nettoyage du fichier de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename=log_file)

# Lancement du crawler
logging.info(f"Lancement du crawl pour : {args.base_url}")
crawler = WebCrawler(
    base_url=args.base_url,
    max_pages=args.max_urls,
    num_threads=args.num_threads,
    delay_seconds=args.politeness_delay
)
crawler.start_crawling()

# Sauvegarde des résultats
logging.info(f"Sauvegarde des données dans : {args.output_path}")
crawler.save_results_to_json(args.output_path)
