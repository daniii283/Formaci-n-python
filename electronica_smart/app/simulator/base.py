from abc import ABC, abstractmethod

class BaseSimulator(ABC):
    def __init__(self, device_id: int):
        self.device_id = device_id

    @abstractmethod
    def simulate(self):
        """Simula el comportamiento del dispositivo"""
        pass