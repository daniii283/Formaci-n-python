from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class SmartDevice(Base):
    __tablename__ = "smart_devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


  