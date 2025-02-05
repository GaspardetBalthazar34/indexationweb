from logger import logger

def process_reviews(product_data):
    """Construit l'index des avis avec la moyenne et le dernier avis."""
    review_index = {}

    for product_id, data in product_data.items():
        reviews = data["reviews"]
        if reviews:
            total_reviews = len(reviews)
            avg_rating = sum(r["rating"] for r in reviews) / total_reviews
            latest_rating = reviews[-1]["rating"]

            review_index[product_id] = {
                "total_reviews": total_reviews,
                "average_rating": round(avg_rating, 2),
                "latest_rating": latest_rating,
            }

    logger.info(f"Analyse des avis terminée : {len(review_index)} produits avec notes moyennes calculées.")
    return review_index
