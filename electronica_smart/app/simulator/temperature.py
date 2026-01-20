import random
from app.simulator.base import BaseSimulator

class TemperatureSimulator(BaseSimulator):
    def __init__(self, device_id: int):
        super().__init__(device_id)
    
    def simulate(self)-> float:
        """Simula una lectura de temperatura en ºC"""
        return round(random.uniform(18.0, 28.0), 2)
    