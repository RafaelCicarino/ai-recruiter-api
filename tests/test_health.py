import os

os.environ["DATABASE_URL"] = "sqlite:///./test_ai_recruiter.db"

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "status": "online",
        "project": "AI Recruiter API",
    }