from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class ClockInSchema(BaseModel):
    email: EmailStr = Field(...)
    location: str = Field(..., max_length=100)
    insert_datetime: Optional[datetime] = Field(None)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "johnkr@email.com",
                "location": "New York",
            }
        }
