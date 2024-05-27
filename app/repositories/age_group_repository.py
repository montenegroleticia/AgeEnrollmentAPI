from bson import ObjectId
from app.db.database import get_database

db = get_database()

async def get_age_groups():
    age_groups = await db.age_groups.find().to_list(100)
    for age_group in age_groups:
        if "_id" in age_group:
            age_group["_id"] = str(age_group["_id"])
    return age_groups
