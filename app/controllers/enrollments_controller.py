from fastapi import HTTPException
from bson.objectid import ObjectId
from app.schemas.enrollments_schemas import EnrollmentCreate
from app.services.enrollments_service import check_enrollment_status_service, register_enrollments_service, view_enrollments_service

async def register_enrollment(enrollment: EnrollmentCreate):
    return await register_enrollments_service(enrollment)

async def check_enrollment_status(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    status = await check_enrollment_status_service(id)
    if status is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return status

async def view_enrollments():
    return await view_enrollments_service()
