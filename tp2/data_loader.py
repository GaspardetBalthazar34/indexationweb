import json
from logger import logger

def load_jsonl(filepath):
    """Charge un fichier JSONL ligne par ligne pour éviter une consommation excessive de mémoire."""
    products = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    products.append(json.loads(line))
                except json.JSONDecodeError:
                    logger.warning(f"Ligne ignorée à cause d'une erreur JSON : {line[:100]}...")

    except FileNotFoundError:
        logger.error(f"Le fichier {filepath} est introuvable.")
    
    logger.info(f"Chargement de {len(products)} produits depuis {filepath}.")
    return products
