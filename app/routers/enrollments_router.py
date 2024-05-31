import threading
from fastapi import APIRouter
from contextlib import asynccontextmanager
from app.controllers.enrollments_controller import check_enrollment_status, register_enrollment, view_enrollments
from app.queue.enrollment_queue import EnrollmentQueue
from app.schemas.enrollments_schemas import EnrollmentCreate

enrollments_router = APIRouter()

enrollment_queue = EnrollmentQueue()

processing_thread = threading.Thread(target=enrollment_queue.process_enrollments)
processing_thread.start()

@enrollments_router.post("/", response_model=str)
async def post_enrollment(enrollment: EnrollmentCreate):
    await register_enrollment(enrollment.age)
    return enrollment_queue.add_enrollment(enrollment)

@enrollments_router.get("/{id}/status", response_model=str)
async def get_enrollment_status(id: str):
    return await check_enrollment_status(id)

@enrollments_router.get("/")
async def get_enrollments():
    return await view_enrollments()

@asynccontextmanager
async def lifespan(router: APIRouter):
    yield
    enrollment_queue.stop_processing()
    processing_thread.join()
