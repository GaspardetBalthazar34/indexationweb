# WebCrawler

This project is a web crawler that browses websites, extracts relevant data (title, first paragraph, and links), and saves the results in a JSON file. It adheres to `robots.txt` rules and includes features such as politeness delay and multithreading for optimized performance.

## Features

- **Respect for **``: Ensures compliance with site rules before accessing pages.
- **Data extraction**: Captures page titles, first paragraphs, and links.
- **Multithreading**: Supports concurrent requests for faster crawling.
- **Politeness delay**: Prevents overloading servers by spacing out requests.
- **Output storage**: Saves extracted data in a structured JSON file.
- **URL validation**: Checks if the provided URL is reachable before crawling.

## Utility Modules

- ``: Converts URLs into valid filenames by removing protocols and replacing special characters.
- ``: Fetches and returns the HTML content of a given URL, handling errors gracefully.
- ``: Verifies if a URL is accessible (HTTP status 200-299) before crawling.

## Usage

### Prerequisites

- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`

### Running the Crawler

Use the following command:

```bash
python main.py -b <base_url> -m <max_urls> -t <n_threads> -p <politeness_delay> -o <output_path>
```

### Parameters

- `-b, --base_url` : Starting URL (default: `https://web-scraping.dev/products`).
- `-m, --max_urls` : Max pages to crawl (default: `5`).
- `-t, --n_threads` : Number of threads (default: `5`).
- `-p, --politeness_delay` : Delay between requests in seconds (default: `5`).
- `-o, --output_path` : Path for the output JSON file (default: `output/crawled_data.json`).

### Example

Crawl 10 pages from `https://web-scraping.dev/products` using 3 threads and a 3-second delay:

```bash
python main.py -b https://web-scraping.dev/products -m 10 -t 3 -p 3 -o output/crawled_data.json
```

## Project Structure

- `main.py` : Entry point, handles arguments and starts the crawler.
- `webcrawler.py` : Implements the crawling logic.
- `utils/filenamesanitizer.py` : Handles filename sanitization.
- `utils/pagedownloader.py` : Downloads webpage content.
- `utils/validurl.py` : Validates URLs.
- `output/` : Stores JSON results and logs.

## Output

- `` : Extracted data in JSON format.
- `` : Logs of the crawling process.

