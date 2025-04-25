# web_search_tool.py
import requests
from bs4 import BeautifulSoup

def web_search(query, num_results=5):
    """Mock web search tool using Google search scraping."""
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"q": query, "num": num_results}
    url = f"https://www.google.com/search"
    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for g in soup.select("div.tF2Cxc")[:num_results]:
        title = g.select_one("h3").text if g.select_one("h3") else ""
        snippet = g.select_one(".VwiC3b").text if g.select_one(".VwiC3b") else ""
        link = g.select_one("a")["href"] if g.select_one("a") else ""
        results.append({"title": title, "link": link, "snippet": snippet})
    return results

