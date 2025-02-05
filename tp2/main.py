import json
from src.data_loader import load_jsonl
from src.index_builder import build_indexes
from src.search_engine import search
from src.ranking import rank_results
from src.logger import logger

# File paths
PRODUCTS_FILE = "data/products.jsonl"
SYNONYMS_FILE = "data/origin_synonyms.json"

# Load products
products = load_jsonl(PRODUCTS_FILE)

# Build indexes
indexes = build_indexes(products)

# Example query
query = "chocolate gift"
results = search(query, indexes)

# Rank results
ranked_results = rank_results(results, indexes)

# Save output
with open("data/search_results.json", "w") as f:
    json.dump(ranked_results, f, indent=4)

logger.info("Search results saved to data/search_results.json")
