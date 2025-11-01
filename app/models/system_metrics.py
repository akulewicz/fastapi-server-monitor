from pydantic import BaseModel
from typing import Optional, List

class CPUInfo(BaseModel):
    brand: Optional[str] = None
    arch: Optional[str] = None
    bits: Optional[int] = None
    temp: Optional[float] = None


class DiskInfo(BaseModel):
    total: Optional[int] = None
    used: Optional[int] = None
    free: Optional[int] = None
    percent: Optional[float] = None


class SystemInfo(BaseModel):
    system: Optional[str] = None
    release: Optional[str] = None
    distro: Optional[str] = None


class MemoryInfo(BaseModel):
    total: Optional[int] = None
    used: Optional[int] = None
    percent: Optional[float] = None

class ConnectedUser(BaseModel):
    name: str 
    host: Optional[str] = None

class UsersInfo(BaseModel):
    connected_users: Optional[List[ConnectedUser]] = None