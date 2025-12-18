from fastapi import APIRouter
from app.api.v1 import solve, limits, health

api_router = APIRouter()

api_router.include_router(solve.router, prefix="/v1", tags=["solve"])
api_router.include_router(limits.router, prefix="/v1", tags=["limits"])
api_router.include_router(health.router, prefix="/v1", tags=["health"])

