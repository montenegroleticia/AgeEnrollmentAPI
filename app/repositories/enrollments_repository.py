from app.db.database import get_database
from app.models.enrollments_model import Enrollment

db = get_database()

async def create_enrollment(enrollment: Enrollment):
    result = await db.enrollments.insert_one(enrollment.model_dump())
    return str(result.inserted_id)

async def get_enrollments():
    enrollments = await db.enrollments.find().to_list(100)
    for age_group in enrollments:
        if "_id" in age_group:
            age_group["_id"] = str(age_group["_id"])
    return enrollments
