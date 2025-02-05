import re
import logging

STOPWORDS = {"the", "a", "an", "of", "in", "to", "is", "on", "for", "with"}

def preprocess_text(text):
    """Tokenise le texte et supprime les stopwords."""
    text = re.sub(r"[^\w\s]", "", text.lower())
    tokens = text.split()
    return [word for word in tokens if word not in STOPWORDS]

def extract_product_id(url):
    """Extrait l'ID produit depuis l'URL."""
    match = re.search(r"/product/(\d+)", url)
    return match.group(1) if match else None

def setup_logging(log_file):
    """Configure le logging vers un fichier."""
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")
