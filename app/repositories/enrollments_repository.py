from bson import ObjectId
from app.db.database import get_database
from app.models.enrollments_model import Enrollment

db = get_database()

async def create_enrollment(enrollment: Enrollment):
    enrollment_dict = enrollment.model_dump()
    enrollment_dict["status"] = "pending"
    result = await db["enrollments"].insert_one(enrollment_dict)
    return str(result.inserted_id)

async def find_enrollment_status(id: str):
    enrollment = await db.enrollments.find_one({"_id": ObjectId(id)})
    return enrollment["status"] if enrollment else None

async def get_enrollments():
    enrollments = await db.enrollments.find().to_list(100)
    for enrollment in enrollments:
        if "_id" in enrollment:
            enrollment["_id"] = str(enrollment["_id"])
    return enrollments
