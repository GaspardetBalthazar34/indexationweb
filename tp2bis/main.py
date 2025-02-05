from data_loader import load_jsonl
from product_processor import process_products
from review_processor import process_reviews
from index_builder import build_inverted_index
import json

# Chargement des données
input_file = "products.jsonl"
products = load_jsonl(input_file)

# Traitement des produits
product_data = process_products(products)

# Création des index
index_title = build_inverted_index(product_data, "title")
index_description = build_inverted_index(product_data, "description")

# Création de l'index des avis
review_index = process_reviews(product_data)

# Sauvegarde des résultats
output_data = {
    "index_title": index_title,
    "index_description": index_description,
    "review_index": review_index
}

with open("indexed_output.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4)

print("Indexation terminée. Résultats enregistrés dans 'indexed_output.json'.")
