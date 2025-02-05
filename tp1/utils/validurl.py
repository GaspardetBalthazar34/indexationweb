import logging
from urllib import request, error

def is_valid_url(url):
    """Validate if the URL is reachable using urllib."""
    try:
        response = request.urlopen(url, timeout=10)
        if 200 <= response.status < 300:
            return True
        else:
            logging.error(f"URL validation failed. Status code: {response.status} for {url}")
            return False
    except error.URLError as e:
        logging.error(f"URL validation error: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error validating URL {url}: {e}")
        return False