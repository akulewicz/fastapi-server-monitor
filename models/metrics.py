from pydantic import BaseModel
from .system import CPUInfo, MemoryInfo, DiskInfo, SystemInfo

class SystemMetrics(BaseModel):
    cpu: CPUInfo
    memory: MemoryInfo
    disk: DiskInfo
    system: SystemInfo