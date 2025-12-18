from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.limiter import get_limits
from app.schemas.limits import LimitsResponse

router = APIRouter()


@router.get("/limits", response_model=LimitsResponse)
async def limits_endpoint(
    device_id: str = Query(...),
    db: Session = Depends(get_db)
):
    limits = get_limits(db, device_id)
    return limits

