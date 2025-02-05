from utils import extract_product_id, extract_variant
from logger import logger

def process_products(products):
    """Regroupe les produits et normalise les variantes."""
    product_data = {}

    for product in products:
        product_id = extract_product_id(product.get("url"))
        if not product_id:
            continue  # Ignore les pages générales

        if product_id not in product_data:
            product_data[product_id] = {
                "title": product.get("title", ""),
                "description": product.get("description", ""),
                "features": product.get("product_features", {}),
                "variants": set(),
                "reviews": [],
            }

        variant = extract_variant(product.get("url"))
        if variant:
            product_data[product_id]["variants"].add(variant)

        product_data[product_id]["reviews"].extend(product.get("product_reviews", []))

    for product_id in product_data:
        product_data[product_id]["variants"] = list(product_data[product_id]["variants"])

    logger.info(f"Normalisation terminée : {len(product_data)} produits regroupés.")
    return product_data
