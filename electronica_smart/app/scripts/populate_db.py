# app/scripts/populate_db.py

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.models.smart_device import SmartDevice
from app.models.device_event_log import DeviceEventLog
from app.core.security import get_password_hash
from faker import Faker
from random import choice, uniform
from datetime import datetime, timedelta

fake = Faker()

device_types = ["Sensor de Temperatura", "Cámara", "Enchufe Inteligente", "Termostato", "Detector de Movimiento"]

def create_users_and_devices(db: Session):
    for _ in range(20):
        username = fake.user_name()
        email = fake.email()
        hashed_password = get_password_hash("123456")

        user = User(username=username, email=email, hashed_password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)

        for _ in range(5):
            device = SmartDevice(
                name=fake.word().capitalize() + " " + choice(["Room", "Device", "Unit"]),
                type=choice(device_types),
                location=fake.city(),
                status=choice([True, False]),
                battery_level=round(uniform(20, 100), 2),
                temperature=round(uniform(15.0, 30.0), 2),
                is_online=True,
                owner_id=user.id,
                last_active=datetime.utcnow() - timedelta(hours=choice(range(10)))
            )
            db.add(device)
            db.commit()
            db.refresh(device)

            for _ in range(3):  # 3 logs por dispositivo
                log = DeviceEventLog(
                    device_id=device.id,
                    event_type="temperature_update",
                    description=f"Simulación de log para {device.name}",
                    temperature=device.temperature,
                    battery_level=device.battery_level,
                    is_online=device.is_online,
                    timestamp=datetime.utcnow() - timedelta(minutes=choice(range(1000)))
                )
                db.add(log)
            db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    create_users_and_devices(db)
    db.close()
    print("✅ Base de datos poblada con datos de prueba.")
