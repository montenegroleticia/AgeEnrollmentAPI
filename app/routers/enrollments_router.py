from app.schemas.enrollments_schemas import EnrollmentCreate
from fastapi import APIRouter
from app.controllers.enrollments_controller import register_enrollment, view_enrollments

enrollments_router = APIRouter()

@enrollments_router.post("/", response_model=str)
async def post_enrollment(enrollment: EnrollmentCreate):
    return await register_enrollment(enrollment)

@enrollments_router.get("/")
async def get_enrollments():
    return await view_enrollments()
