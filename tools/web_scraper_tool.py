# web_scraper_tool.py
import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    """Extracts main text content from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        texts = soup.stripped_strings
        return " ".join(texts)[:3000]  # token-safe limit
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"
