from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.fastapi.trace import FastAPITraceMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import logging
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://frontend-app.calmflower-2ea9ee62.westeurope.azurecontainerapps.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Telemetry: Tracing middleware
FastAPITraceMiddleware(
    app,
    exporter=AzureExporter(
        connection_string=f"InstrumentationKey={os.environ['APPINSIGHTS_INSTRUMENTATIONKEY']}"
    ),
    sampler=ProbabilitySampler(1.0),
)

# Telemetry: Logging handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(
    AzureLogHandler(
        connection_string=f"InstrumentationKey={os.environ['APPINSIGHTS_INSTRUMENTATIONKEY']}"
    )
)

@app.get("/quote")
def quote():
    logger.info("Quote endpoint hit")
    return {"quote": "This is a placeholder quote"}
