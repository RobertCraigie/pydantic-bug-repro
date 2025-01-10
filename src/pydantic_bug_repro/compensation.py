from __future__ import annotations

from typing import Optional
from pydantic import BaseModel
from ._compat import PYDANTIC_V2


class Compensation(BaseModel):
    worker: Optional[Worker] = None
    worker_id: Optional[str] = None


from .worker import Worker

if PYDANTIC_V2:
    Compensation.model_rebuild()
else:
    Compensation.update_forward_refs()  # type: ignore
