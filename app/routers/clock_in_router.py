from fastapi import APIRouter, HTTPException
from services.clock_in_service import (
    create_clock_in,
    get_clock_in_by_id,
    delete_clock_in,
    update_clock_in,
    filter_clock_ins,
)
from schema.user_clock_in import ClockInSchema
from config.utils import ResponseModel
from fastapi.encoders import jsonable_encoder

router = APIRouter()


def clock_in_helper(clock_in) -> dict:
    return {
        "id": str(clock_in["_id"]),
        "email": clock_in["email"],
        "location": clock_in["location"],
        "insert_datetime": clock_in["insert_datetime"],
    }


@router.post("/clock-in")
async def create(clock_in: ClockInSchema):
    new_record_id = await create_clock_in(clock_in)
    new_record = await get_clock_in_by_id(new_record_id)
    return ResponseModel(clock_in_helper(new_record), "record created successfully")


@router.get("/clock-in/filter")
async def filter_data(
    email: str = None, location: str = None, insert_datetime: str = None
):
    result = await filter_clock_ins(email, location, insert_datetime)
    result = [clock_in_helper(doc) for doc in result]
    return result
    return ResponseModel(result, "record fetched successfully")


@router.get("/clock-in/{id}")
async def read(id: str):
    clock_in = await get_clock_in_by_id(id)
    if clock_in:
        return ResponseModel(clock_in_helper(clock_in), "record created successfully")
    raise HTTPException(status_code=404, detail="record not found")


@router.delete("/clock-in/{id}")
async def delete(id: str):
    result = await delete_clock_in(id)
    if not result:
        raise HTTPException(status_code=404, detail="record not found")
    return ResponseModel({}, "record deleted successfully")


@router.put("/clock-in/{id}")
async def update(id: str, clock_in: ClockInSchema):
    check_record = await get_clock_in_by_id(id)
    if not check_record:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_record = await update_clock_in(id, jsonable_encoder(clock_in))
    if not updated_record:
        raise HTTPException(status_code=400, detail="Failed to update record")

    updated_record_data = await get_clock_in_by_id(id)

    return ResponseModel(
        clock_in_helper(updated_record_data), "recod updated successfully"
    )
