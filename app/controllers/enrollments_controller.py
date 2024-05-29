from app.schemas.enrollments_schemas import EnrollmentCreate
from app.services.enrollments_service import register_enrollments_service, view_enrollments_service

async def register_enrollment(enrollment: EnrollmentCreate):
    return await register_enrollments_service(enrollment)

async def view_enrollments():
    return await view_enrollments_service()
