from fastapi import APIRouter
from app.controllers.age_group_controller import register_age_group, remove_age_group, view_age_groups
from app.schemas.age_group_schema import AgeGroupCreate

age_groups_router = APIRouter()

@age_groups_router.post("/", response_model=str)
async def post_age_group(age_group: AgeGroupCreate):
    return await register_age_group(age_group)

@age_groups_router.get("/")
async def get_age_groups():
    return await view_age_groups()

@age_groups_router.delete("/{id}", response_model=int)
async def delete_age_group(id: str):
    return await remove_age_group(id)
