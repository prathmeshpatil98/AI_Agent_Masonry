# tests/test_tools.py

import pytest
from tools.content_analyzer_tool import analyze_content
from tools.web_scraper_tool import scrape_content
from tools.web_search_tool import web_search
from tools.news_aggregator_tool import fetch_news
import os


def test_analyze_content():
    text = "Meditation helps reduce stress, improve focus and enhance well-being."
    keywords = ["meditation", "focus", "stress"]
    result = analyze_content(text, keywords)

    assert result["relevant"] is True
    assert result["relevance_score"] >= 2
    assert isinstance(result["summary"], str)


def test_scrape_content_valid_url():
    url = "https://www.example.com"
    content = scrape_content(url)
    assert isinstance(content, str)
    assert len(content) > 0 or "Scrape Error" in content


def test_web_search_results():
    results = web_search("open source ai tools", num_results=3)
    assert isinstance(results, list)
    assert len(results) <= 3
    assert all("title" in r and "link" in r and "snippet" in r for r in results)


@pytest.mark.skipif(not os.getenv("NEWS_API_KEY"), reason="NEWS_API_KEY not set")
def test_fetch_news_results():
    news = fetch_news("climate change", page_size=3)
    assert isinstance(news, list)
    assert len(news) <= 3
    for item in news:
        assert "headline" in item
        assert "url" in item
