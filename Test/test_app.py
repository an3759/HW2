import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Project')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, GitHub Actions!"
    assert "generatedAt" in data
    assert data["generatedAt"].startswith("20")