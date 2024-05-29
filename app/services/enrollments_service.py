from app.repositories.enrollments_repository import create_enrollment, get_enrollments
from app.schemas.enrollments_schemas import EnrollmentCreate

async def register_enrollments_service(enrollment: EnrollmentCreate):
    return await create_enrollment(enrollment)

async def view_enrollments_service():
    return await get_enrollments()
