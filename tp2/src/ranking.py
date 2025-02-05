def rank_results(results, indexes):
    """Rank search results using review scores."""
    ranked_results = []
    
    for product_id in results:
        review_data = indexes["reviews"].get(product_id, {"average_rating": 0, "total_reviews": 0})
        score = review_data["average_rating"] * review_data["total_reviews"]
        ranked_results.append((product_id, score))
    
    return sorted(ranked_results, key=lambda x: x[1], reverse=True)
