from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from datetime import datetime, timezone
from app.models.device import Device
from app.models.request import Request


def get_today_usage(db: Session, device_id: str) -> int:
    """Count requests created today for a device."""
    today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    used_today = db.query(func.count(Request.id)).filter(
        and_(
            Request.device_id == device_id,
            Request.created_at >= today_start
        )
    ).scalar() or 0
    return used_today


def get_limits(db: Session, device_id: str) -> dict:
    """Get daily limits for a device."""
    # Get or create device
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        device = Device(id=device_id, is_subscribed=False)
        db.add(device)
        db.commit()
        db.refresh(device)
    
    # Count requests today
    used_today = get_today_usage(db, device_id)
    
    daily_limit = 5
    
    return {
        "daily_limit": daily_limit,
        "used_today": used_today,
        "subscription": device.is_subscribed
    }

