from app.services.enrollments_service import view_enrollments_service

async def view_enrollments():
    return await view_enrollments_service()
