from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class DeviceEventLog(Base):
    __tablename__ = "device_event_logs"

    id = Column(Integer, primary_key = True, index = True)
    device_id = Column(Integer, ForeignKey("smart_devices.id"), nullable = False)
    timestamp = Column(DateTime(timezone=True), server_default = func.now())
    event_type = Column(String(50), nullable = False)
    description = Column(String(255), nullable = True)
    temperature = Column(Float, nullable = True)
    battery_level = Column(Float, nullable = True)
    is_online = Column(Integer, nullable = False)

    device = relationship("SmartDevice", backref = "event_logs")



