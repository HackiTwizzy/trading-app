from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Beispiel-Daten
market_data = {
    "stocks": [
        {"ticker": "AMD", "price": 278.26, "change_percent": 5.17, "score": 90, "setup": "Momentum Spike", "verdict": "strong"},
        {"ticker": "NVDA", "price": 198.24, "change_percent": 0.92, "score": 45, "setup": "leichter Trend", "verdict": "schwach"},
        {"ticker": "AAPL", "price": 214.10, "change_percent": 1.12, "score": 62, "setup": "Trendaufbau", "verdict": "gut"},
    ],
    "crypto": [
        {"ticker": "BTCUSD", "price": 70250, "change_percent": 2.10, "score": 75, "setup": "Trend Continuation", "verdict": "good"},
        {"ticker": "ETHUSD", "price": 3520, "change_percent": 1.44, "score": 68, "setup": "Breakout", "verdict": "gut"},
        {"ticker": "SOLUSD", "price": 88.28, "change_percent": -0.99, "score": 35, "setup": "kein Setup", "verdict": "schwach"},
    ],
    "commodities": [
        {"ticker": "USOIL", "price": 82.40, "change_percent": -1.20, "score": 35, "setup": "kein Setup", "verdict": "schwach"},
        {"ticker": "XAUUSD", "price": 2357.40, "change_percent": 0.37, "score": 45, "setup": "leichter Trend", "verdict": "neutral"},
    ]
}


def get_all_assets():
    all_assets = []
    for category, items in market_data.items():
        for item in items:
            item_copy = item.copy()
            item_copy["category"] = category
            all_assets.append(item_copy)
    return all_assets


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    all_assets = get_all_assets()
    top_signals = sorted(all_assets, key=lambda x: x["score"], reverse=True)[:6]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "Trading Dashboard",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "top_signals": top_signals,
        "stocks": market_data["stocks"],
        "crypto": market_data["crypto"],
        "commodities": market_data["commodities"],
    })


@app.get("/health")
def health():
    return {
        "status": "ok",
        "server": "running",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.get("/api/market")
def api_market():
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": market_data
    }


@app.get("/api/search/{ticker}")
def search_ticker(ticker: str):
    all_assets = get_all_assets()
    result = [x for x in all_assets if x["ticker"].lower() == ticker.lower()]

    if not result:
        return {"found": False, "ticker": ticker.upper()}

    return {"found": True, "result": result[0]}
