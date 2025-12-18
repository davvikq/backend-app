from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(String, primary_key=True)
    device_id = Column(String, ForeignKey("devices.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    tokens_used = Column(Integer, default=0)
    success = Column(Boolean, default=False)

