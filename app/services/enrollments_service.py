from app.repositories.enrollments_repository import get_enrollments

async def view_enrollments_service():
    return await get_enrollments()
