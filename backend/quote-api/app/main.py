from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.quotes import get_random_quote

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3001",
        "https://frontend-app--5mgubcy.wittydesert-2d99a67b.westeurope.azurecontainerapps.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/quote")
def quote():
    return {"quote": get_random_quote()}
