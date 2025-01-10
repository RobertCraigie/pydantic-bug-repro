from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel

if TYPE_CHECKING:
    from .worker import Worker


class Compensation(BaseModel):
    worker: Optional[Worker] = None
    worker_id: Optional[str] = None

    model_config = {'defer_build': True}
