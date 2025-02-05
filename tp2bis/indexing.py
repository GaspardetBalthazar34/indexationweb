from collections import defaultdict
from utils import preprocess_text, extract_product_id
import logging

def create_indexes(products):
    """Crée les index pour les titres, descriptions, reviews et features."""
    
    index_title = defaultdict(list)
    index_description = defaultdict(list)
    index_reviews = {}
    index_features = defaultdict(list)

    for product in products:
        product_id = extract_product_id(product["url"])
        
        # Indexation des titres
        tokens = preprocess_text(product.get("title", ""))
        for token in tokens:
            index_title[token].append(product_id)

        # Indexation des descriptions
        tokens = preprocess_text(product.get("description", ""))
        for token in tokens:
            index_description[token].append(product_id)

        # Indexation des reviews
        reviews = product.get("product_reviews", [])
        if reviews:
            index_reviews[product_id] = {
                "total_reviews": len(reviews),
                "average_rating": sum(r["rating"] for r in reviews) / len(reviews),
                "latest_rating": reviews[-1]["rating"]
            }

        # Indexation des features
        features = product.get("product_features", {})
        for key, value in features.items():
            index_features[f"{key}:{value}"].append(product_id)

    logging.info("Indexation terminée.")
    return {
        "index_title": index_title,
        "index_description": index_description,
        "index_reviews": index_reviews,
        "index_features": index_features
    }
