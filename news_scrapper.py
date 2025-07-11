import feedparser

def fetch_news(keyword):
    query = keyword.replace(" ", "+")
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=en&gl=PK&ceid=PK:en"
    feed = feedparser.parse(rss_url)

    news_list = []
    for entry in feed.entries[:2]:  # get top 2 articles
        news_list.append({
            "title": entry.title,
            "url": entry.link,
            "source": entry.get("source", {}).get("title", "Unknown"),
            "snippet": entry.get("summary", ""),
        })
    return news_list
