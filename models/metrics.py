from pydantic import BaseModel
from .system import CPUInfo, MemoryInfo, DiskInfo, SystemInfo
from .rpi_metrics import RPiEnvInfo

class SystemMetrics(BaseModel):
    cpu: CPUInfo
    memory: MemoryInfo
    disk: DiskInfo
    system: SystemInfo
    env: RPiEnvInfo