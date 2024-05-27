import asyncio
from app.db.database import create_db_and_collections

async def main():
    await create_db_and_collections()

if __name__ == "__main__":
    asyncio.run(main())
