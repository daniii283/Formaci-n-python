from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SmartDeviceBase(BaseModel):
  name: str
  type: str
  location: str
  status: bool = False

class SmartDeviceCreate(SmartDeviceBase):
  pass

class SmartDeviceRead(SmartDeviceBase):
  id: int
  created_at: datetime

  class Config:
    from_attributes = True

class SmartDeviceUpdate(BaseModel):
  name: Optional[str] = None
  type: Optional[str] = None
  location: Optional[str] = None
  status: Optional[bool] = None
  