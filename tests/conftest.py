import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import get_database

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
async def test_db():
    db = get_database()
    yield db
