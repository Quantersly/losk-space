from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PropertyResponse(BaseModel):
    id: int
    developer_id: int
    building: str
    floor: int
    apartment_number: str
    area: float
    rooms: Optional[int]
    price: Optional[float]
    address: Optional[str]
    status: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True