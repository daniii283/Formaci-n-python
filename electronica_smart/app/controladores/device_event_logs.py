from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.services import device_event_log_service as service
from app.schemas.device_event_log import DeviceEventLogRead

router = APIRouter(prefix="/logs", tags=["Logs de Dispositivos"])

@router.get("/{device_id}", response_model=List[DeviceEventLogRead])
def get_logs(device_id: int, db: Session = Depends(get_db)):
    return service.get_device_logs(db, device_id)
