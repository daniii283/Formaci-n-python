from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.models.smart_device import SmartDevice
from app.schemas.simulation import SimulationInput
from app.schemas.device_event_log import DeviceEventLogCreate
from app.services import device_event_log_service as log_service

router = APIRouter(prefix="/simulate", tags=["Simulation"])


@router.post("/temperature/{device_id}")
def simulate_temperature(
    device_id: int,
    data: SimulationInput,
    db: Session = Depends(get_db),
):
    device = db.query(SmartDevice).filter(SmartDevice.id == device_id).first()

    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")

    # Conversión de temperatura
    if data.unit == "K":
        new_temp = data.temperature - 273.15
    elif data.unit == "ºF":
        new_temp = (data.temperature - 32) * 5 / 9
    else:
        new_temp = data.temperature

    # Actualizar dispositivo
    device.temperature = new_temp
    device.last_active = datetime.utcnow()
    device.is_online = True

    db.commit()
    db.refresh(device)

    # ✅ CREAR LOG CORRECTAMENTE (objeto Pydantic)
    log_data = DeviceEventLogCreate(
        device_id=device.id,
        event_type="temperature_update",
        description=f"Temperatura actualizada a {new_temp:.2f} ºC",
        temperature=new_temp,
        battery_level=device.battery_level,
        is_online=device.is_online
    )

    log_service.log_event(db, log_data)

    return {
        "message": "Simulación actualizada",
        "temperature_celsius": round(new_temp, 2)
    }
