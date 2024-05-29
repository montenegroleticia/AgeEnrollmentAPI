from fastapi import APIRouter
from app.controllers.enrollments_controller import view_enrollments

enrollments_router = APIRouter()

@enrollments_router.get("/")
async def get_enrollments():
    return await view_enrollments()
