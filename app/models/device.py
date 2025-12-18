from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(String, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_subscribed = Column(Boolean, default=False)

