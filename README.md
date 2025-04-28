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

1. Input: Instagram
2. Output: Average Sentiment Score: 0.45
3. Number of Reviews Analyzed: 100

## Tech Stack

1. Frontend: React (TypeScript)
2. Backend: FastAPI (Python)
3. Sentiment Analysis: TextBlob

## Video Explanation Link :

https://drive.google.com/file/d/1xjGgipll9e3-WU3MGBzi7AuofJ5zhS5z/view?usp=sharing

## Setup Instructions

### Backend

1. Navigate to the backend folder:
   ```bash
   cd backend
   
2. Install dependencies:
  ```bash
  pip install fastapi uvicorn nltk

3. Run the backend server:
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
