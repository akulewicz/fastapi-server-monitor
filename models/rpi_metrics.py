from pydantic import BaseModel
from typing import Optional

class RPiEnvInfo(BaseModel):
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    pressure: Optional[float] = None