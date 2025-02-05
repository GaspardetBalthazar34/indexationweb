import re
from collections import defaultdict
from utils import tokenize
from logger import logger

def build_inverted_index(data, field):
    """Construit un index inversé pour un champ donné (ex: title, description)."""
    index = defaultdict(set)

    for product_id, product in data.items():
        tokens = tokenize(product.get(field, ""))
        for token in tokens:
            index[token].add(product_id)

    logger.info(f"Indexation terminée pour {field}: {len(index)} termes indexés.")
    return {k: list(v) for k, v in index.items()}
