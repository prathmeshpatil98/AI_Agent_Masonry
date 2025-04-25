
import os
import requests
from datetime import datetime, timedelta

def fetch_news(query, page_size=5):
    """
    Fetches the most recent news articles matching `query` from NewsAPI.
    Input:   query (str), page_size (int)
    Output:  list of dicts with keys: headline, summary, url, source
    """
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError("❌ NEWS_API_KEY not found in environment!")
    
    url = "https://newsapi.org/v2/everything"
    from_date = (datetime.utcnow() - timedelta(days=7)).strftime("%Y-%m-%d")
    
    params = {
        "q": query,
        "from": from_date,
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": api_key
    }
    resp = requests.get(url, params=params, timeout=10)
    data = resp.json()
    
    articles = []
    for art in data.get("articles", []):
        articles.append({
            "headline": art.get("title"),
            "summary": art.get("description") or art.get("content") or "",
            "url": art.get("url"),
            "source": art.get("source", {}).get("name")
        })
    return articles
