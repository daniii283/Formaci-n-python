from app.simulator.temperature import TemperatureSimulator

def simulate_temperature_for_device(device_id: int)-> dict:
    simulator = TemperatureSimulator(device_id)
    temperature = simulator.simulate()
    return {
        "device_id": device_id,
        "temperature": temperature,
        "unit": "ºC"
    }