from pydantic import BaseModel
from typing import Literal

class SimulationInput(BaseModel):
    temperature: float
    unit: Literal["ºC", "K", "ºF"]
