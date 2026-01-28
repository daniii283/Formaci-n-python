from sqlalchemy.orm import Session
from app.models.smart_device import SmartDevice
from app.models.device_event_log import DeviceEventLog
from app.repositories import device_event_log_repository as repo

def log_event(db: Session, log_data: dict) -> DeviceEventLog:
    device = db.query(SmartDevice).filter(
        SmartDevice.id == log_data["device_id"]
    ).first()

    if not device:
        raise ValueError("Dispositivo no encontrado")

    # Completar valores si no vienen
    log_data.setdefault("is_online", device.is_online)
    log_data.setdefault("battery_level", device.battery_level)
    log_data.setdefault("temperature", device.temperature)

    log = DeviceEventLog(**log_data)
    return repo.create_log(db, log)

def get_device_logs(db: Session, device_id: int):
    return repo.get_logs_by_device(db, device_id)
