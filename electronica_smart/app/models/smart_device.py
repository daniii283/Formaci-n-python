from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class SmartDevice(Base):
    __tablename__ = "smart_devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # ✅ Campos corregidos
    battery_level = Column(Float, default = 100.0)
    last_active = Column(DateTime, nullable = True)
    temperature = Column(Float, nullable = True)
    is_online = Column(Boolean, default = False)

    # Relaciones
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="devices")



  