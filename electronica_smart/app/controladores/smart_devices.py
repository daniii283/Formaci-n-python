from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.smart_device import SmartDeviceCreate, SmartDeviceRead, SmartDeviceUpdate
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.smart_device_service import (
    create_device_for_user,
    get_all_devices_for_user,
    get_device_by_id_for_user,
    update_device_for_user,
    delete_device_for_user
)

router = APIRouter(prefix="/devices", tags=["Smart Devices"])

@router.post("/", response_model=SmartDeviceRead)
def create_device(device: SmartDeviceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_device_for_user(db, device, current_user)

@router.get("/", response_model=List[SmartDeviceRead])
def read_all_devices(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_devices_for_user(db, current_user)

@router.get("/{device_id}", response_model=SmartDeviceRead)
def read_device_by_id(device_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_device_by_id_for_user(db, device_id, current_user)

@router.put("/{device_id}", response_model=SmartDeviceRead)
def update_device_by_id(device_id: int, device_data: SmartDeviceUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_device_for_user(db, device_id, device_data, current_user)

@router.delete("/{device_id}")
def delete_device_by_id(device_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return delete_device_for_user(db, device_id, current_user)
