from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, status
from app.models.smart_device import SmartDevice
from app.models.user import User
from app.schemas.smart_device import SmartDeviceCreate, SmartDeviceUpdate
from app.repositories import smart_device_repository as repo

def create_device_for_user(db: Session, device_data: SmartDeviceCreate, user: User) -> SmartDevice:
    return repo.create_device(db, device_data, owner_id=user.id)

def get_all_devices_for_user(db: Session, user: User) -> List[SmartDevice]:
    return db.query(SmartDevice).filter(SmartDevice.owner_id == user.id).all()

def get_device_by_id_for_user(db: Session, device_id: int, user: User) -> SmartDevice:
    device = repo.get_device_by_id(db, device_id)
    if not device:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Device not found")
    if device.owner_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this device")
    return device

def update_device_for_user(db: Session, device_id: int, device_data: SmartDeviceUpdate, user: User) -> SmartDevice:
    device = get_device_by_id_for_user(db, device_id, user)
    return repo.update_device(db, device, device_data)

def delete_device_for_user(db: Session, device_id: int, user: User) -> dict:
    device = get_device_by_id_for_user(db, device_id, user)
    repo.delete_device(db, device)
    return {"detail": "Device deleted successfully"}
