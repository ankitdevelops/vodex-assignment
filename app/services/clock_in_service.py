from datetime import datetime
from config.db import ClockInRecords
from bson import ObjectId


async def create_clock_in(clock_in: dict):
    clock_in_dict = clock_in.dict()
    clock_in_dict["insert_datetime"] = datetime.utcnow()
    result = await ClockInRecords.insert_one(clock_in_dict)
    return str(result.inserted_id)


async def get_clock_in_by_id(id: str):
    return await ClockInRecords.find_one({"_id": ObjectId(id)})


async def delete_clock_in(id: str):
    result = await ClockInRecords.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0


async def update_clock_in(id: str, clock_in_data: dict):
    result = await ClockInRecords.update_one(
        {"_id": ObjectId(id)}, {"$set": clock_in_data}
    )
    return result.modified_count > 0


async def filter_clock_ins(email=None, location=None, insert_datetime=None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        insert_datetime = datetime.strptime(insert_datetime, "%Y-%m-%d")
        query["insert_datetime"] = {"$gt": insert_datetime}
    result = await ClockInRecords.find(query).to_list()
    return result
