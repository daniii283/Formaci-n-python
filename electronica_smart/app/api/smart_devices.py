from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.smart_device import SmartDeviceCreate, SmartDeviceRead, SmartDeviceUpdate
from app.db.session import get_db
from app.repositories.smart_device_repository import(
  create_device,
  get_all_devices,
  get_device_by_id,
  update_device,
  delete_device
) 

router = APIRouter(prefix="/devices", tags=["Smart Devices"])

@router.post("/", response_model=SmartDeviceRead)
def create_Device(device: SmartDeviceCreate, db: Session = Depends(get_db)):
  return create_device(db, device)

@router.get("/", response_model=List[SmartDeviceRead])
def read_all_devices(db: Session = Depends(get_db)):
  return get_all_devices(db)

@router.get("/{device_id}", response_model=SmartDeviceRead)
def read_device_by_id(device_id: int, db: Session = Depends(get_db)):
  return get_device_by_id(db, device_id)

@router.put("/{device_id}", response_model=SmartDeviceRead)
def update_device_by_id(device_id: int, device_data: SmartDeviceUpdate, db: Session = Depends(get_db)):
  return update_device(db, device_id, device_data)

@router.delete("/{device_id}")
def delete_device_by_id(device_id: int, db: Session = Depends (get_db)):
  return delete_device(db, device_id)
  
  