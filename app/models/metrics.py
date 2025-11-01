from pydantic import BaseModel
from .system_metrics import CPUInfo, MemoryInfo, DiskInfo, SystemInfo, UsersInfo
from .rpi_metrics import RPiEnvInfo
from .network_metrics import NetworkInfo

class SystemMetrics(BaseModel):
    cpu: CPUInfo
    memory: MemoryInfo
    disk: DiskInfo
    system: SystemInfo
    users: UsersInfo
    env: RPiEnvInfo
    network: NetworkInfo