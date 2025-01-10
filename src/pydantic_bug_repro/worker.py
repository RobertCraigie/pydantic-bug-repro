# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from pydantic import BaseModel
from ._compat import PYDANTIC_V2


class Worker(BaseModel):
    compensation: Optional[Compensation] = None

    legal_entity: Optional[LegalEntity] = None

    manager: Optional[Worker] = None


from .compensation import Compensation
from .legal_entity import LegalEntity

if PYDANTIC_V2:
    Worker.model_rebuild()
else:
    Worker.update_forward_refs()  # type: ignore
