from fastapi import APIRouter
from services.system_metrics import get_system_metrics
from services.rpi_metrics import get_rpi_env
from services.network_metrics import get_network_info
from models.metrics import SystemMetrics

router = APIRouter()

@router.get("/api/status", response_model=SystemMetrics)
async def get_all_metrics():
    system_data = get_system_metrics()
    rpi_data = get_rpi_env()
    network_data = get_network_info()
    return SystemMetrics(
        cpu=system_data["cpu"],
        memory=system_data["memory"],
        disk=system_data["disk"],
        system=system_data["system"],
        users=system_data["users"],
        env=rpi_data,
        network=network_data
    )