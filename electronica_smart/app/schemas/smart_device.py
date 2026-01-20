from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SmartDeviceBase(BaseModel):
  name: str
  type: str
  location: Optional[str] = None
  status: Optional[bool] = True

class SmartDeviceCreate(SmartDeviceBase):
  pass

class SmartDeviceUpdate(BaseModel):
  name: Optional[str]
  type: Optional[str]
  location: Optional[str]
  status: Optional[bool]

class SmartDeviceRead(SmartDeviceBase):
  id: int
  baterry_level: float
  last_Active: datetime
  temperature: Optional[float]
  is_online: bool

  class Config:
    from_attributes = True


  