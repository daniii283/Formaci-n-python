from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class SmartDevice(Base):
    __tablename__ = "smart_devices"

    # Atributos
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    baterry_level = Float
    last_active = DateTime
    temperature = Float
    is_online = Boolean
    
    # Relaciones
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="devices")


  