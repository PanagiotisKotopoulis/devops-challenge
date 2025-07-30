from fastapi import FastAPI
from app.quotes import get_random_quote

app = FastAPI()

@app.get("/quote")
def quote():
    return {"quote": get_random_quote()}