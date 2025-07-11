from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from news_scrapper import fetch_news
from sentiment import analyze_sentiment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    keyword = data.get("keyword")

    if not keyword:
        return {"error": "No keyword provided!"}

    articles = fetch_news(keyword)

    if not articles:
        return {
            "good": 0,
            "bad": 0,
            "average": 0,
            "summary": "No daily news article found for your search keyword."
        }

    texts = []
    for a in articles:
        parts = [a.get("title", ""), a.get("source", "")]
        if "snippet" in a:
            parts.append(a["snippet"])
        texts.append(". ".join([p for p in parts if p]))

    result = analyze_sentiment(texts)
    return result


