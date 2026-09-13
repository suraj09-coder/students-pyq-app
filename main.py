from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online", "message": "PYQ Aggregator API is running"}
