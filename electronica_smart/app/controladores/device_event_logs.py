from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services import device_event_log_service as service
from app.schemas.device_event_log import DeviceEventLogCreate, DeviceEventLogRead
from app.core.dependencies import get_current_user
from app.models.user import User 

router = APIRouter(prefix="/logs", tags=["Logs de Dispositivos"])

@router.post("/", response_model=DeviceEventLogRead)
def create_log(
    log_data: DeviceEventLogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ✅ Añadido
):
    return service.log_event(db, log_data)

@router.get("/{device_id}", response_model=List[DeviceEventLogRead])
def get_logs(device_id: int, db: Session = Depends(get_db)):
    return service.get_device_logs(db, device_id)
