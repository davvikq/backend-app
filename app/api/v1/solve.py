from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
import uuid
from app.core.database import get_db
from app.services.solver import solve
from app.services.limiter import get_today_usage
from app.schemas.solve import SolveResponse
from app.models.request import Request
from app.models.device import Device

router = APIRouter()

DAILY_LIMIT = 5


@router.post("/solve", response_model=SolveResponse)
async def solve_endpoint(
    image: UploadFile = File(...),
    language: str = Form(...),
    device_id: str = Form(...),
    grade: Optional[int] = Form(None),
    subject_hint: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    # Validate language
    if language not in ["ru", "uz"]:
        raise HTTPException(status_code=400, detail="Language must be 'ru' or 'uz'")
    
    # Check daily limit
    used_today = get_today_usage(db, device_id)
    if used_today >= DAILY_LIMIT:
        raise HTTPException(status_code=429, detail="Daily limit exceeded")
    
    # Ensure device exists
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        try:
            device = Device(id=device_id, is_subscribed=False)
            db.add(device)
            db.commit()
            db.refresh(device)
        except Exception:
            db.rollback()
            raise HTTPException(status_code=500, detail="Database error")
    
    # Solve the task
    result = await solve(image, language, grade, subject_hint)
    
    # Record request
    try:
        request = Request(
            id=str(uuid.uuid4()),
            device_id=device_id,
            tokens_used=0,
            success=True
        )
        db.add(request)
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    
    return result

