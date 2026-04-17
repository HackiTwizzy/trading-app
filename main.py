from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "läuft", "msg": "Trading Bot Online"}
