from bson import ObjectId  # type: ignore
from config.db import Item
from datetime import datetime, timezone


async def create_item(item_data: dict):

    item_data["insert_date"] = datetime.now(timezone.utc)
    item = await Item.insert_one(item_data)
    return str(item.inserted_id)


async def get_item_by_id(item_id: str):
    return await Item.find_one({"_id": ObjectId(item_id)})


async def update_item(item_id: str, item_data: dict):
    if "insert_date" in item_data:
        del item_data["insert_date"]
    updated_item = await Item.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": item_data},
    )
    return updated_item.modified_count > 0


async def delete_item(id: str):
    result = await Item.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0


async def filter_items(email=None, expiry_date=None, insert_date=None, quantity=None):
    query = {}
    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gt": expiry_date}
    if insert_date:
        insert_date = datetime.strptime(insert_date, "%Y-%m-%d")
        query["insert_date"] = {"$gt": insert_date}
    if quantity:
        query["quantity"] = {"$gte": quantity}
    return await Item.find(query).to_list(None)


async def aggregate_items_by_email():
    return await Item.aggregate(
        [{"$group": {"_id": "$email", "count": {"$sum": 1}}}]
    ).to_list(None)
