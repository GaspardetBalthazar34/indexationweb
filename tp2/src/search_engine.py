from src.utils import tokenize

def search(query, indexes):
    """Search for matching products based on indexed data."""
    tokens = tokenize(query)
    results = set()

    for token in tokens:
        if token in indexes["title"]:
            results.update(indexes["title"][token])
        if token in indexes["description"]:
            results.update(indexes["description"][token])
    
    return list(results)
