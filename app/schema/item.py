from typing import Optional
from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr, Field


class ItemSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    item_name: str = Field(...)
    quantity: int = Field(..., gt=0)
    expiry_date: datetime = Field(..., gt=datetime.today())
    insert_date:Optional[datetime] = Field(None)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Kumar",
                "email": "johnkr@email.com",
                "item_name": "Test Item",
                "quantity": 2,
                "expiry_date": datetime.today(),
            }
        }
