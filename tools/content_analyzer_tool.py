# content_analyzer_tool.py
def analyze_content(raw_text, keywords):
    """Fake analyzer: checks if keywords exist and scores relevance."""
    score = sum(1 for word in keywords if word.lower() in raw_text.lower())
    is_relevant = score >= len(keywords) // 2
    return {
        "relevance_score": score,
        "relevant": is_relevant,
        "summary": raw_text[:500] + "..."
    }


