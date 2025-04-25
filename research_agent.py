# # research_agent.py

# from tools.news_aggregator_tool import fetch_news
# from tools.web_search_tool import web_search
# from tools.web_scraper_tool import scrape_content
# from tools.content_analyzer_tool import analyze_content
# from llm_connector import query_gemini

# def research_agent(query):
#     print(f"🔍 Starting research on: {query}\n")

#     # 1. Search the web for information related to the query
#     search_results = web_search(query)
#     search_section = "### 1. Web Search Results\n"
#     for i, res in enumerate(search_results, start=1):
#         search_section += f"{i}. [{res['title']}]({res['link']}) — {res['snippet']}\n"
#     if not search_results:
#         search_section += "No results found.\n"

#     # 2. Extract relevant data from those websites
#     extracted_texts = []
#     for res in search_results:
#         text = scrape_content(res["link"])
#         extracted_texts.append((res["link"], text))
#     extract_section = "### 2. Extracted Data\n"
#     for url, text in extracted_texts:
#         extract_section += f"- **{url}**: {text[:200]}...\n"
#     if not extracted_texts:
#         extract_section += "No data extracted.\n"

#     # 3. Find and summarize latest news articles
#     try:
#         news_items = fetch_news(query)
#     except Exception as e:
#         news_items = []
#     news_section = "### 3. Latest News Articles\n"
#     for item in news_items:
#         news_section += f"- **{item['headline']}** ({item['source']}): {item['url']}\n  > {item['summary']}\n"
#     if not news_items:
#         news_section += "No news found.\n"

#     # 4. Crawl pages for any additional structured information
#     # (here we reuse scraping + analyzer to simulate “crawling”)
#     crawled = []
#     for url, text in extracted_texts:
#         analysis = analyze_content(text, query.split())
#         crawled.append((url, analysis))
#     crawl_section = "### 4. Crawled Pages Analysis\n"
#     for url, analysis in crawled:
#         crawl_section += (
#             f"- **{url}**: Relevant={analysis['relevant']}, "
#             f"Score={analysis['relevance_score']}\n"
#             f"  Summary: {analysis['summary']}\n"
#         )
#     if not crawled:
#         crawl_section += "No pages crawled.\n"

#     # 5. Compile and present a comprehensive report
#     prompt = f"""
# You are Masonry’s autonomous Web Research Agent. Perform the following tasks on the user’s query:

# {search_section}

# {extract_section}

# {news_section}

# {crawl_section}

# ### 5. Final Comprehensive Report
# Based on all of the above, write a single, well-structured report that:
# - Summarizes key findings
# - Highlights any data, timelines, or statistics
# - Cites sources inline (e.g., [1], [2])
# - Uses clear headings and bullet points
# """
#     final_report = query_gemini(prompt)
#     return final_report

# if __name__ == "__main__":
#     topic = input("🧠 Enter research topic: ")
#     print("\n📝 Research Report:\n")
#     print(research_agent(topic))
#     print("\n---\n")
#     print("🔍 Research completed.")

# research_agent.py

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