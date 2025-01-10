from __future__ import annotations

from typing import Optional
from pydantic import BaseModel
from ._compat import PYDANTIC_V2


class LegalEntity(BaseModel):
    id: str
    parent: Optional[LegalEntity] = None
    parent_id: Optional[str] = None


if PYDANTIC_V2:
    LegalEntity.model_rebuild()
else:
    LegalEntity.update_forward_refs()  # type: ignore
