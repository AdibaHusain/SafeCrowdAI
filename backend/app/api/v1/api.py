from fastapi import APIRouter
from app.api.v1.endpoints import crowd_detection

api_router = APIRouter()
api_router.include_router(crowd_detection.router, prefix="/crowd", tags=["Crowd Detection"])
