from app.repositories.age_group_repository import get_age_groups

async def view_age_groups_service():
    return await get_age_groups()
