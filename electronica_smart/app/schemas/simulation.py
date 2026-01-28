from pydantic import BaseModel
from typing import Optional

class SimulationInput(BaseModel):
   temperature: Optional[float] = None
   battery_level: Optional[float] = None
   is_online: Optional[bool] = None
   status: Optional[bool] = None
   unit: Optional[str] = "ºC" #default

   