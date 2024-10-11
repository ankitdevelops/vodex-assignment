import os
from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGODB_URL")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["fastapi_db"]
Item = database.get_collection("items")
ClockInRecords = database.get_collection("clock_in_records")
