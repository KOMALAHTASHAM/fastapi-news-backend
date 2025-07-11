from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

def analyze_sentiment(news_list):
    sid = SentimentIntensityAnalyzer()
    pos = neg = neu = 0
    summary = ""

    for news in news_list:
        score = sid.polarity_scores(news)
        if score["compound"] >= 0.05:
            pos += 1
        elif score["compound"] <= -0.05:
            neg += 1
        else:
            neu += 1
        summary += f"{news}\n\n"

    total = max(1, pos + neg + neu)
    return {
        "good": round((pos / total) * 100, 2),
        "bad": round((neg / total) * 100, 2),
        "average": round((neu / total) * 100, 2),
        "summary": summary[:250] + "..."
    }
