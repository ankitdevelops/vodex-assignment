from fastapi import APIRouter, HTTPException, Body
from config.utils import ResponseModel
from schema.item import ItemSchema
from services.item_service import (
    create_item,
    get_item_by_id,
    update_item,
    delete_item,
    filter_items,
    aggregate_items_by_email,
)
from fastapi.encoders import jsonable_encoder

router = APIRouter()


def item_helper(item) -> dict:
    if "count" in item and "_id" in item:
        return {"email": item["_id"], "count": item["count"]}
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "item_name": item["item_name"],
        "quantity": item["quantity"],
        "expiry_date": item["expiry_date"],
        "insert_date": item["insert_date"],
    }


@router.post("/items")
async def create_item_api(item: ItemSchema = Body(...)):
    item = jsonable_encoder(item)
    new_item_id = await create_item(item)
    new_item = await get_item_by_id(new_item_id)
    return ResponseModel(item_helper(item), "item created successfully")


@router.get("/items/filter")
async def filter(
    email: str = None,
    expiry_date: str = None,
    insert_date: str = None,
    quantity: int = None,
):
    result = await filter_items(email, expiry_date, insert_date, quantity)
    result = [item_helper(doc) for doc in result]
    return ResponseModel(result, "record fetched successfully")


@router.get("/items/aggregate")
async def aggregate_item():
    records = await aggregate_items_by_email()
    result = [item_helper(doc) for doc in records]
    return ResponseModel(result, "record fetched successfully")


@router.get("/items/{item_id}")
async def get_item_api(item_id: str):
    item = await get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ResponseModel(item_helper(item), "record fetched successfully")


@router.put("/items/{item_id}")
async def update_item_api(item_id: str, item: ItemSchema = Body(...)):
    check_item = await get_item_by_id(item_id)
    if not check_item:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = await update_item(item_id, jsonable_encoder(item))

    if not updated_item:
        raise HTTPException(status_code=400, detail="Failed to update item")

    updated_item_data = await get_item_by_id(item_id)

    return ResponseModel(item_helper(updated_item_data), "Item updated successfully")


@router.delete("/items/{id}")
async def delete(id: str):
    result = await delete_item(id)
    if not result:
        raise HTTPException(status_code=404, detail="record not found")
    return ResponseModel({}, "record deleted successfully")
