from app.repositories.enrollments_repository import create_enrollment, find_enrollment_status, get_enrollments
from app.schemas.enrollments_schemas import EnrollmentCreate

async def register_enrollments_service(enrollment: EnrollmentCreate):
    return await create_enrollment(enrollment)

async def check_enrollment_status_service(id: str):
    return await find_enrollment_status(id)

async def view_enrollments_service():
    return await get_enrollments()
