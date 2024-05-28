from app.schemas.age_group_schema import AgeGroupCreate
from fastapi import APIRouter
from app.services.age_group_service import register_age_group_service, view_age_groups_service

age_groups_router = APIRouter()

@age_groups_router.post("/", response_model=str)
async def register_age_group(age_group: AgeGroupCreate):
    return await register_age_group_service(age_group)

@age_groups_router.get("/")
async def view_age_groups():
    return await view_age_groups_service()
