from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB URL (Default to local if not set)
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "social_media_db")

client = AsyncIOMotorClient(MONGO_URL)
database = client[DB_NAME]

# Collections helpers
users_collection = database["users"]
drafts_collection = database["drafts"]
schedules_collection = database["schedules"]
