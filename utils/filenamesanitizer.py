import re

def generate_sanitized_filename(url):
    """Sanitize the URL to create a valid filename."""
    # Remove 'http://' or 'https://'
    url = re.sub(r"^https?://", "", url)
    # Replace non-alphanumeric characters with underscores
    sanitized = re.sub(r"[^\w\-_.]", "_", url)
    # Remove trailing underscores
    sanitized = re.sub(r"_+$", "", sanitized)
    return sanitized
