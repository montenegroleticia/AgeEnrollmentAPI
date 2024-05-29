import pytest
from httpx import AsyncClient

@pytest.mark.asyncio(scope='module')
async def test_create_age_group(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as async_client:
        response = await async_client.post("/age-groups/", json={"min_age": 18, "max_age": 25})
        assert response.status_code == 200
        assert isinstance(response.json(), str)

@pytest.mark.asyncio(scope='module')
async def test_get_age_groups(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as async_client:
        response = await async_client.get("/age-groups/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio(scope='module')
async def test_delete_age_group(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as async_client:
        response = await async_client.post("/age-groups/", json={"min_age": 26, "max_age": 35})
        age_group_id = response.json()
        response = await async_client.delete(f"/age-groups/{age_group_id}")
        assert response.status_code == 200
        assert response.json() == 1

@pytest.mark.asyncio(scope='module')
async def test_delete_age_group_not_found(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as async_client:
        age_group_id = '665639423ad22f92d5c712fe'
        response = await async_client.delete(f"/age-groups/{age_group_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Age group not found"}

@pytest.mark.asyncio(scope='module')
async def test_enrollments(test_app):
    async with AsyncClient(app=test_app, base_url="http://test_enrollments") as async_client:
        response = await async_client.get("/enrollments/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
