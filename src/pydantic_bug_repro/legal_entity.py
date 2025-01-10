from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class LegalEntity(BaseModel):
    id: str
    parent: Optional[LegalEntity] = None
    parent_id: Optional[str] = None
