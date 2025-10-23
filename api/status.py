from fastapi import APIRouter
from services.system_metrics import get_system_metrics
from models.metrics import SystemMetrics

router = APIRouter()

@router.get("/api/status", response_model=SystemMetrics)
async def get_all_metrics():
    return get_system_metrics()