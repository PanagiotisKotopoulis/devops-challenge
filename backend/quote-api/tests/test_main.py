# backend/tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app  # Adjust the import based on your project structure

client = TestClient(app)

def test_get_quote():
    response = client.get("/quote")
    assert response.status_code == 200
    assert "quote" in response.json()
