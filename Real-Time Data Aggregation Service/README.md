
# Real Time Forex Tracker

## Thought Process

Users need reliable forex rates.
Public APIs sometimes fail.

Solution:
- Multiple APIs
- Fallback
- Cache
- Freshness indicator

## Tech Stack

Backend: FastAPI
Frontend: React

## How To Run

Backend

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Frontend

npx create-react-app frontend
Replace src/App.js with provided file
npm start

## Endpoint

GET /rates
