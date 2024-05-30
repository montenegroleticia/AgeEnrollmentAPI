from bson import ObjectId
from app.db.database import get_database

db = get_database()

async def find_enrollment_status(id: str):
    enrollment = await db.enrollments.find_one({"_id": ObjectId(id)})
    return enrollment["status"] if enrollment else None

async def get_enrollments():
    enrollments = await db.enrollments.find().to_list(100)
    for enrollment in enrollments:
        if "_id" in enrollment:
            enrollment["_id"] = str(enrollment["_id"])
    return enrollments
