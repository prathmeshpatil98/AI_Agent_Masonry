from tools.news_aggregator_tool import fetch_news
from tools.web_search_tool import web_search
from tools.web_scraper_tool import scrape_content
from tools.content_analyzer_tool import analyze_content
from llm_connector import query_gemini

def research_agent(query):
    print(f"🔍 Researching: {query}")

    # Step 1: Fetch latest news articles
    try:
        news_items = fetch_news(query)
    except Exception as e:
        print(f"⚠️ News API error: {e}")
        news_items = []

    # Build the “Recent News” section
    if news_items:
        news_section = "### 📰 Recent News Articles\n"
        for n in news_items:
            news_section += (
                f"- **{n['headline']}** ({n['source']}): {n['url']}\n"
                f"  > {n['summary']}\n"
            )
    else:
        news_section = "### 📰 No recent news found. Falling back to general web search.\n"

    # Step 2: Web Search + Scrape for additional context
    search_results = web_search(query)
    contents = []
    for res in search_results:
        raw = scrape_content(res["link"])
        analyzed = analyze_content(raw, query.split())
        if analyzed["relevant"]:
            contents.append(f"**Source:** {res['link']}\n{analyzed['summary']}")

    web_section = (
        "### 🌐 Additional Web Sources\n" + "\n\n".join(contents)
        if contents
        else "### 🌐 No relevant web content found.\n"
    )

    # Step 3: Dynamic, generic prompt
    prompt = f"""
You are Masonry’s autonomous Web Research AI Agent.

Your goal is to **automatically** search the web, extract relevant and Perfect information and compile a **comprehensive research report** that answers the user’s query _with minimal human input_.  
- Include a **concise summary**  
- Highlight **key findings**  
- Provide any relevant **data, timelines, or if there are any statistics**  
- **Cite sources inline** where possible  

#### User’s Query:
\"\"\"{query}\"\"\"

{news_section}

{web_section}
"""
    # Step 4: Call Gemini
    summary = query_gemini(prompt)
    return summary

if __name__ == "__main__":
    topic = input("🧠 Enter research topic: ")
    print("\n📝 Research Report:\n")
    print(research_agent(topic))