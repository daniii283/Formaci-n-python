from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.models.smart_device import SmartDevice
from app.schemas.simulation import SimulationInput
from app.services import device_event_log_service as log_service

router = APIRouter(prefix="/simulate", tags=["Simulation"])

@router.post("/{device_id}")
def unified_simulation(
    device_id: int,
    data: SimulationInput,
    db: Session = Depends(get_db),
):
    device = db.query(SmartDevice).filter(SmartDevice.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")

    description_parts = []
    log_data = {
        "device_id": device_id,
        "event_type": "simulation_update",
    }

    # Comparar y actualizar temperatura
    if data.temperature is not None:
        original_temp = device.temperature
        if data.unit == "K":
            new_temp = data.temperature - 273.15
        elif data.unit == "ºF":
            new_temp = (data.temperature - 32) * 5 / 9
        else:
            new_temp = data.temperature

        if original_temp != new_temp:
            device.temperature = new_temp
            description_parts.append(
                f"Temperatura cambiada de {original_temp:.2f} ºC a {new_temp:.2f} ºC"
            )
            log_data["temperature"] = new_temp

    # Comparar y actualizar batería
    if data.battery_level is not None and data.battery_level != device.battery_level:
        description_parts.append(
            f"Batería cambió de {device.battery_level}% a {data.battery_level}%"
        )
        device.battery_level = data.battery_level
        log_data["battery_level"] = data.battery_level

    # Comparar y actualizar estado online
    if data.is_online is not None and data.is_online != device.is_online:
        description_parts.append(
            f"Estado online cambiado de {device.is_online} a {data.is_online}"
        )
        device.is_online = data.is_online
        log_data["is_online"] = data.is_online

    # Actualizar última actividad
    device.last_active = datetime.utcnow()
    db.commit()

    # Crear log solo si hubo cambios
    if description_parts:
        log_data["description"] = " | ".join(description_parts)
        log_service.log_event(db, log_data)

    return {"message": "Simulación procesada correctamente"}
