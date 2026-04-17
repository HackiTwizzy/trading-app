from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


# 🔹 Startseite
@app.get("/")
def home():
    return {
        "app": "Trading Bot",
        "status": "online",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# 🔹 Health Check (für später Monitoring)
@app.get("/health")
def health():
    return {
        "status": "ok",
        "server": "running"
    }


# 🔹 Fake Signals (später kommt dein echter Scanner hier rein)
@app.get("/scan")
def scan():
    signals = [
        {
            "ticker": "AMD",
            "price": 278.26,
            "change_percent": 5.17,
            "score": 90,
            "setup": "Momentum Spike",
            "verdict": "strong",
            "reasons": [
                "hohes Volumen",
                "starker Trend",
                "Momentum bestätigt"
            ]
        },
        {
            "ticker": "BTCUSD",
            "price": 70250,
            "change_percent": 2.1,
            "score": 75,
            "setup": "Trend Continuation",
            "verdict": "good",
            "reasons": [
                "Trend stabil",
                "Volumen steigt"
            ]
        },
        {
            "ticker": "USOIL",
            "price": 82.4,
            "change_percent": -1.2,
            "score": 35,
            "setup": "kein Setup",
            "verdict": "schwach",
            "reasons": [
                "kein klares Signal"
            ]
        }
    ]

    return {
        "count": len(signals),
        "signals": signals
    }
