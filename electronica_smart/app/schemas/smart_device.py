from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SmartDeviceBase(BaseModel):
  name: str
  type: str
  location: Optional[str] = None
  status: Optional[bool] = None

class SmartDeviceCreate(SmartDeviceBase):
  pass

class SmartDeviceUpdate(BaseModel):
  name: Optional[str]
  type: Optional[str]
  location: Optional[str]
  status: Optional[bool] = None

class SmartDeviceRead(SmartDeviceBase):
  id: int
  battery_level: float
  last_active: Optional[datetime]
  temperature: Optional[float]
  is_online: bool

  class Config:
    from_attributes = True


  