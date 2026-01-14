from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.smart_device import SmartDevice
from app.schemas.smart_device import SmartDeviceCreate, SmartDeviceUpdate

def create_device(db: Session, device: SmartDeviceCreate):
  new_device = SmartDevice(**device.dict())
  db.add(new_device)
  db.commit()
  db.refresh(new_device)
  return new_device

def get_all_devices(db: Session):
  return db.query(SmartDevice).all()

def get_device_by_id(db: Session, device_id: int):
  device = db.query(SmartDevice).filter(SmartDevice.id == device_id).first()
  if not device:
    raise HTTPException(status_code=404, detail="Device not found")
  return device

def update_device(db: Session, device_id: int, device_data: SmartDeviceUpdate):
  device = db.query(SmartDevice).filter(SmartDevice.id == device_id).first()
  if not device:
    raise HTTPException(status_code=404, detail="DEvice not found")
  for field, value in device_data.dict(exclude_unset=True).items():
    setattr(device, field, value)

  db.commit()
  db.refresh(device)
  return device
  

def delete_device(db: Session, device_id: int):
  device = db.query(SmartDevice).filter(SmartDevice.id == device_id).first()
  if not device:
    raise HTTPException(status_code=404, detail="Device not found")
  db.delete(device)
  db.commit()
  return {"message": "Device deleted successfully"}

