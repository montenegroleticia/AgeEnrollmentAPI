from app.models.age_group_model import AgeGroup
from app.repositories.age_group_repository import create_age_group, get_age_groups
from app.schemas.age_group_schema import AgeGroupCreate

async def register_age_group_service(age_group: AgeGroupCreate):
    age_group_id = await create_age_group(age_group)
    return age_group_id

async def view_age_groups_service():
    return await get_age_groups()
