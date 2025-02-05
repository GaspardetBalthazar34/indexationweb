from utils import extract_product_id, extract_variant
from logger import logger

def process_products(products):
    """Regroupe les produits et normalise les variantes tout en validant les données d'entrée."""
    product_data = {}

    for product in products:
        # Vérification des champs essentiels
        if "url" not in product:
            logger.warning("Produit ignoré : pas d'URL.")
            continue
        
        product_id = extract_product_id(product["url"])
        if not product_id:
            continue  # Ignore les pages générales
        
        if product_id not in product_data:
            product_data[product_id] = {
                "title": product.get("title", "Titre inconnu"),
                "description": product.get("description", "Description non fournie"),
                "features": product.get("product_features", {}),
                "variants": set(),
                "reviews": [],
            }

        # Gestion des variantes
        variant = extract_variant(product["url"])
        if variant:
            product_data[product_id]["variants"].add(variant)

        # Ajout des avis tout en gérant les doublons
        existing_reviews = {r["id"] for r in product_data[product_id]["reviews"]}  # Ensemble des IDs d'avis existants
        for review in product.get("product_reviews", []):
            if "id" not in review or review["id"] in existing_reviews:
                continue  # Ignorer les avis sans ID ou déjà présents
            product_data[product_id]["reviews"].append(review)
            existing_reviews.add(review["id"])

    # Conversion des variantes en liste pour compatibilité JSON
    for product_id in product_data:
        product_data[product_id]["variants"] = list(product_data[product_id]["variants"])

    logger.info(f"Normalisation terminée : {len(product_data)} produits regroupés.")
    return product_data
