from sqlalchemy.orm import Session
from app.models.device_event_log import DeviceEventLog
from app.schemas.device_event_log import DeviceEventLogCreate

def create_log(db: Session, log_data):
    log = DeviceEventLog(**log_data.model_dump())
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_log_by_device(db: Session, device_id: int):
    return db.query(DeviceEventLog).filter(DeviceEventLog.id == device_id).order_by(DeviceEventLog.timestamp.desc()).all()


