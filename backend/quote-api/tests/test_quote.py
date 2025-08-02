# backend/quote-api/tests/test_quote.py

import sys
import os
from fastapi.testclient import TestClient

# Ensure the app module is discoverable regardless of working directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app.main import app

client = TestClient(app)

def test_get_quote():
    response = client.get("/quote")
    assert response.status_code == 200
    assert "quote" in response.json()
