import json
import logging
from data_loader import load_jsonl
from indexing import create_indexes
from utils import setup_logging

# Initialisation des logs
setup_logging("output.log")

# Fichier d'entrée contenant les produits
input_file = "products.jsonl"

# Chargement des données
products = load_jsonl(input_file)

# Création des index
indexes = create_indexes(products)

# Sauvegarde des index
with open("indexed_output.json", "w") as f:
    json.dump(indexes, f, indent=4)

logging.info("Indexation terminée avec succès.")