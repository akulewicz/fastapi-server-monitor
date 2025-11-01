from typing import Optional
from pydantic import BaseModel


class NetworkInfo(BaseModel):
    hostname: Optional[str] = None
    ip: Optional[str] = None