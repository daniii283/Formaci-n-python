from fastapi import APIRouter, Depends
from app.services.simulation_service import simulate_temperature_for_device
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/simulate", tags=["Simulation"])

@router.get("/temperature/{device_id}")
def simulate_temperature(device_id: int, current_user: User = Depends(get_current_user)):
    return simulate_temperature_for_device(device_id)
