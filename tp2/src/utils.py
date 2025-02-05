import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def tokenize(text):
    """Tokenizes and cleans text."""
    words = re.findall(r'\b\w+\b', text.lower())
    return [word for word in words if word not in STOPWORDS]

def extract_product_id(url):
    """Extracts product ID from a URL."""
    match = re.search(r'/product/(\d+)', url)
    return match.group(1) if match else None
