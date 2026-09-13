from fastapi import FastAPI
from scraper import fetch_pyqs

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online", "message": "PYQ Aggregator API is running"}

@app.get("/scrape")
def scrape():
    data = fetch_pyqs()
    return {"status": "success", "data": data}
