from src.utils import tokenize, extract_product_id
from collections import defaultdict

def build_indexes(products):
    """Create indexes for search."""
    title_index = defaultdict(list)
    description_index = defaultdict(list)
    review_index = {}

    for product in products:
        product_id = extract_product_id(product["url"])
        
        # Tokenize title
        for token in tokenize(product["title"]):
            title_index[token].append(product_id)
        
        # Tokenize description
        for token in tokenize(product["description"]):
            description_index[token].append(product_id)
        
        # Process reviews
        reviews = product.get("product_reviews", [])
        if reviews:
            review_index[product_id] = {
                "total_reviews": len(reviews),
                "average_rating": sum(r["rating"] for r in reviews) / len(reviews),
                "latest_rating": reviews[-1]["rating"],
            }

    return {
        "title": title_index,
        "description": description_index,
        "reviews": review_index
    }
