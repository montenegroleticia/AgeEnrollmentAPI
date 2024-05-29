from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME]

async def create_db_and_collections():
    await db.create_collection("age_groups")
    await db.create_collection("enrollments")

def get_database():
    return db
