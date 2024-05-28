import pytest
from httpx import AsyncClient
from app.main import app
from app.db.database import get_database

@pytest.mark.asyncio
async def test_create_age_group():
    db = get_database()
    await db.age_groups.drop()

    async with AsyncClient(app=app, base_url="http://test") as async_client:
        response = await async_client.post("/age-groups/", json={"min_age": 18, "max_age": 25})
        assert response.status_code == 200
        assert isinstance(response.json(), str)

    await db.age_groups.drop()

@pytest.mark.asyncio
async def test_get_age_groups():
    db = get_database()
    await db.age_groups.drop()

    async with AsyncClient(app=app, base_url="http://test") as async_client:
        response = await async_client.get("/age-groups/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    await db.age_groups.drop()
