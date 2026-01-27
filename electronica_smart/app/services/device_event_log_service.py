from sqlalchemy.orm import Session
from app.schemas.device_event_log import DeviceEventLogCreate
from app.repositories import device_event_log_repository as repo

def log_event(db: Session, log_data: DeviceEventLogCreate):
    return repo.create_log(db, log_data)

def get_device_logs(db: Session, device_id: int):
    return repo.get_log_by_device(db, device_id)