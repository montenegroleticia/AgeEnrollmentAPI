from app.db.database import get_database

db = get_database()

async def get_enrollments():
    enrollments = await db.enrollments.find().to_list(100)
    for age_group in enrollments:
        if "_id" in age_group:
            age_group["_id"] = str(age_group["_id"])
    return enrollments
