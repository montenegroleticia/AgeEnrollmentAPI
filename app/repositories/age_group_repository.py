from bson import ObjectId
from app.models.age_group_model import AgeGroup
from app.db.database import get_database

db = get_database()

async def create_age_group(age_group: AgeGroup):
    result = await db.age_groups.insert_one(age_group.model_dump())
    return str(result.inserted_id)

async def get_age_groups():
    age_groups = await db.age_groups.find().to_list(100)
    for age_group in age_groups:
        if "_id" in age_group:
            age_group["_id"] = str(age_group["_id"])
    return age_groups
