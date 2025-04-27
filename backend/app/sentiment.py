from textblob import TextBlob

async def analyze_sentiment(text: str) -> float:
    analysis = TextBlob(text)
    return analysis.sentiment.polarity