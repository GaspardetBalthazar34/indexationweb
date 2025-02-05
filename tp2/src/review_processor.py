from logger import logger

def process_reviews(product_data):
    """Construit l'index des avis en supprimant les doublons et en ajoutant les stats."""
    review_index = {}

    for product_id, data in product_data.items():
        reviews = data["reviews"]
        if reviews:
            unique_reviews = {r["id"]: r for r in reviews}.values()  # Suppression des doublons par ID

            total_reviews = len(unique_reviews)
            avg_rating = sum(r["rating"] for r in unique_reviews) / total_reviews
            latest_rating = sorted(unique_reviews, key=lambda r: r["date"], reverse=True)[0]["rating"]

            review_index[product_id] = {
                "total_reviews": total_reviews,
                "average_rating": round(avg_rating, 2),
                "latest_rating": latest_rating,
            }

    logger.info(f"Analyse des avis terminée : {len(review_index)} produits avec notes moyennes calculées.")
    return review_index
