from pydantic import BaseModel
from typing import Optional


class Capability(BaseModel):
    id: int
    name: str
    function: Optional[int] = None
    capability_type: Optional[str] = None
    description: str