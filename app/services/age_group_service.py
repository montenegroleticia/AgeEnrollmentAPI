from app.repositories.age_group_repository import create_age_group, get_age_groups, delete_age_group
from app.schemas.age_group_schema import AgeGroupCreate

async def register_age_group_service(age_group: AgeGroupCreate):
    return await create_age_group(age_group)

async def view_age_groups_service():
    return await get_age_groups()

async def remove_age_group_service(id: str):
    return await delete_age_group(id)
