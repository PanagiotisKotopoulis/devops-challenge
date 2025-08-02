from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.quotes import get_random_quote
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
import os

app = FastAPI()

# App Insights Logging (optional)
instrumentation_key = os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY")
if instrumentation_key:
    logger = logging.getLogger(__name__)
    logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={instrumentation_key}'))

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-app.calmflower-2ea9ee62.westeurope.azurecontainerapps.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/quote")
def quote():
    return {"quote": get_random_quote()}
