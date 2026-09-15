import os

import pytest
from fastapi.testclient import TestClient


os.environ["DATABASE_URL"] = "sqlite:///./test_ai_recruiter.db"

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client