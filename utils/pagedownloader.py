from urllib import request, error

def fetch_page_content(url):
    """
    Downloads the HTML content of a web page.
    """
    try:
        # Sending a request to the URL
        response = request.urlopen(url)
        
        # Reading and decoding the HTML content
        return response.read().decode('utf-8')

    except:
        # Return None if any error occurs
        return None