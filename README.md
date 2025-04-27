# Playstore Sentiment Analyzer

Analyze Google Playstore app reviews and find their average sentiment score.

## Project Structure

- **backend/app/main.py** — FastAPI server exposing `/analyze` endpoint.
- **backend/app/sentiment.py** — Fetches reviews and analyzes sentiment.
- **frontend/src/pages/index.tsx** — React frontend to input app name and display results.

## How It Works

1. User enters an app name on the frontend.
2. Frontend sends a POST request to `/analyze` on the backend.
3. Backend fetches app reviews, performs sentiment analysis, and returns:
   - Average Sentiment Score
   - Number of Reviews Analyzed
4. Frontend displays the results.

## Example

  Input: Instagram
  Output: Average Sentiment Score: 0.45
  Number of Reviews Analyzed: 100

## Tech Stack

  Frontend: React (TypeScript)
  Backend: FastAPI (Python)
  Sentiment Analysis: NLTK VADER

## Setup Instructions

### Backend

1. Navigate to the backend folder:
   ```bash
   cd backend/app
   
2. Install dependencies:
  ```bash
  pip install fastapi uvicorn nltk

3. Download NLTK VADER Lexicon (if not already):
  ```bash
  import nltk
  nltk.download('vader_lexicon')

4. Run the backend server:
  ```bash
  uvicorn main:app --reload

### Frontend

1. Navigate to the frontend folder:
  ```bash
  cd frontend

2. Install dependencies:
  ```bash    
  npm install

3. Start the development server:
  ```bash
  npm run dev
