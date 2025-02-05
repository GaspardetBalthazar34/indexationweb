import re

def extract_product_id(url):
    """Extrait l'ID produit d'une URL donnée."""
    match = re.search(r'/product/(\d+)', url)
    return match.group(1) if match else None

def extract_variant(url):
    """Extrait la variante d'une URL si elle est présente."""
    match = re.search(r'variant=([\w-]+)', url)
    return match.group(1) if match else None

def tokenize(text):
    """Nettoie et tokenize un texte en supprimant la ponctuation et les stopwords basiques."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Supprime la ponctuation
    tokens = text.split()
    return [token for token in tokens if token not in {"the", "and", "is", "in", "on", "at", "of"}]
