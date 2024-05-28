import pytest
import asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from app.main import app
from app.db.database import get_database

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="module")
def test_app():
    return app

@pytest.fixture(scope="module")
async def async_client(test_app: FastAPI):
    async with AsyncClient(app=test_app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module")
async def test_db():
    db = get_database()
    await db.age_groups.drop()
    yield db
    await db.age_groups.drop()
