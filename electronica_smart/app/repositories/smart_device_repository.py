from sqlalchemy.orm import Session
from app.models.smart_device import SmartDevice
from app.schemas.smart_device import SmartDeviceCreate, SmartDeviceUpdate

def create_device(db: Session, device_data: SmartDeviceCreate, owner_id: int) -> SmartDevice:
    db_device = SmartDevice(**device_data.dict(), owner_id=owner_id)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_device_by_id(db: Session, device_id: int) -> SmartDevice | None:
    return db.query(SmartDevice).filter(SmartDevice.id == device_id).first()

def update_device(db: Session, device: SmartDevice, device_data: SmartDeviceUpdate) -> SmartDevice:
    for field, value in device_data.dict(exclude_unset=True).items():
        setattr(device, field, value)
    db.commit()
    db.refresh(device)
    return device

def delete_device(db: Session, device: SmartDevice):
    db.delete(device)
    db.commit()
