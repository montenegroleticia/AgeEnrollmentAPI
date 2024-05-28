from fastapi import APIRouter, HTTPException, status
from app.schemas.age_group_schema import AgeGroupCreate
from app.services.age_group_service import register_age_group_service, view_age_groups_service, remove_age_group_service

age_groups_router = APIRouter()

@age_groups_router.post("/", response_model=str)
async def register_age_group(age_group: AgeGroupCreate):
    return await register_age_group_service(age_group)

@age_groups_router.get("/")
async def view_age_groups():
    return await view_age_groups_service()

@age_groups_router.delete("/{id}", response_model=int)
async def remove_age_group(id: str):
    age_group_count = await remove_age_group_service(id)
    if age_group_count < 1:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Age group not found")
    return age_group_count
