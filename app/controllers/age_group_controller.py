from fastapi import APIRouter
from app.services.age_group_service import view_age_groups_service

age_groups_router = APIRouter()

@age_groups_router.get("/")
async def view_age_groups():
    return await view_age_groups_service()
