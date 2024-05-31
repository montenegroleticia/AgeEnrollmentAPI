from app.repositories.age_group_repository import get_age_groups
from app.repositories.enrollments_repository import find_enrollment_status, get_enrollments

async def check_age_group_exists_for_age(age: int):
    age_groups = await get_age_groups()
    for age_group in age_groups:
        if age_group['min_age'] <= age <= age_group['max_age']:
            return True

    return False

async def check_enrollment_status_service(id: str):
    return await find_enrollment_status(id)

async def view_enrollments_service():
    return await get_enrollments()
