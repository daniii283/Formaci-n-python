from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DeviceEventLogCreate(BaseModel):
    device_id: int
    event_type: str
    description: Optional[str] = None
    temperature: Optional[float] = None
    battery_level: Optional[float] = None
    is_online: Optional[bool] = None

class DeviceEventLogRead(DeviceEventLogCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True