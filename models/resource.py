from typing import List, Optional
from pydantic import BaseModel, Field
from models.capability import Capability


class Resource(BaseModel):
    id: int
    uri: Optional[str] = None
    created_at: str  # Pode ser convertido para datetime, se necessário
    updated_at: str  # Pode ser convertido para datetime, se necessário
    lat: float
    lon: float
    status: str
    collect_interval: Optional[int] = None
    description: str
    uuid: str
    city: Optional[str] = None
    neighborhood: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    capabilities: List[str] = Field(default_factory=list)