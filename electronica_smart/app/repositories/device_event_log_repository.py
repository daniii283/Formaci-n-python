from sqlalchemy.orm import Session
from app.models.device_event_log import DeviceEventLog

def create_log(db: Session, log: DeviceEventLog) -> DeviceEventLog:
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_logs_by_device(db: Session, device_id: int):
    return (
        db.query(DeviceEventLog)
        .filter(DeviceEventLog.device_id == device_id)
        .order_by(DeviceEventLog.timestamp.desc())
        .all()
    )
