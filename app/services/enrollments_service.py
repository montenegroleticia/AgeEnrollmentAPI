from app.repositories.enrollments_repository import find_enrollment_status, get_enrollments
async def check_enrollment_status_service(id: str):
    return await find_enrollment_status(id)

async def view_enrollments_service():
    return await get_enrollments()
