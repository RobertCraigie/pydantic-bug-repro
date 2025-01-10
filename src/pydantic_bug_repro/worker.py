# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel
from .legal_entity import LegalEntity

if TYPE_CHECKING:
    from .compensation import Compensation


class Worker(BaseModel):
    compensation: Optional[Compensation] = None

    legal_entity: Optional[LegalEntity] = None

    manager: Optional[Worker] = None

    model_config = {'defer_build': True}
