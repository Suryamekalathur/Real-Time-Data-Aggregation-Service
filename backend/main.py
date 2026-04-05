
from fastapi import FastAPI
import requests
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cache = {
    "data": None,
    "timestamp": None,
    "source": None
}

def fetch_primary():
    try:
        res = requests.get("https://open.er-api.com/v6/latest/USD", timeout=5)
        data = res.json()
        return {
            "base": data["base_code"],
            "rates": data["rates"],
            "source": "Open ER API",
            "timestamp": datetime.utcnow().isoformat()
        }
    except:
        return None

def fetch_secondary():
    try:
        res = requests.get("https://api.exchangerate.host/latest?base=USD", timeout=5)
        data = res.json()
        return {
            "base": data["base"],
            "rates": data["rates"],
            "source": "ExchangeRate Host",
            "timestamp": datetime.utcnow().isoformat()
        }
    except:
        return None

@app.get("/rates")
def get_rates():
    data = fetch_primary()

    if not data:
        data = fetch_secondary()

    if data:
        cache["data"] = data
        cache["timestamp"] = datetime.utcnow()
        return data

    if cache["data"]:
        return {
            **cache["data"],
            "cached": True
        }

    return {
        "error": "Unable to fetch exchange rates"
    }
