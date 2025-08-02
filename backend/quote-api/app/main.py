from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.quotes import get_random_quote
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
import os

app = FastAPI()

# Logging configuration
instrumentation_key = os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY")
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

if instrumentation_key:
    logger.addHandler(
        AzureLogHandler(connection_string=f'InstrumentationKey={instrumentation_key}')
    )
    logger.info("Application Insights logger initialized.")
else:
    logger.addHandler(logging.StreamHandler())
    logger.info("Logger initialized without Application Insights.")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-app.calmflower-2ea9ee62.westeurope.azurecontainerapps.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.get("/quote")
def quote():
    logger.info("GET /quote called")
    return {"quote": get_random_quote()}
