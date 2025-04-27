from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google_play_scraper import search, reviews, Sort
import asyncio
from app.sentiment import analyze_sentiment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AppRequest(BaseModel):
    appName: str

# New helper function to get package name from app name
async def get_package_name(app_name: str) -> str:
    search_result = search(app_name, lang="en", country="us")
    if not search_result:
        raise HTTPException(status_code=404, detail="App not found in Play Store")
    return search_result[0]["appId"]

@app.post("/analyze")
async def analyze_reviews(request: AppRequest):
    try:
        # Step 1: Get package name from app name
        package_name = await get_package_name(request.appName)

        # Step 2: Fetch reviews
        fetched_reviews, _ = reviews(
            package_name,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=100
        )

        texts = [r['content'] for r in fetched_reviews if r.get('content')]

        if not texts:
            return {
                "message": "No reviews found for the specified app.",
                "average_sentiment_score": None,
                "number_of_reviews": 0
            }

        # Step 3: Analyze sentiment
        sentiment_scores = await asyncio.gather(*(analyze_sentiment(text) for text in texts))

        if not sentiment_scores:
            return {
                "message": "No valid sentiment scores generated.",
                "average_sentiment_score": None,
                "number_of_reviews": 0
            }

        avg_score = sum(sentiment_scores) / len(sentiment_scores)

        return {
            "app_name": request.appName,
            "package_name": package_name,
            "average_sentiment_score": avg_score,
            "number_of_reviews": len(sentiment_scores)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
