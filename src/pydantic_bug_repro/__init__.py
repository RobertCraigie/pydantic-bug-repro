from .legal_entity import LegalEntity as LegalEntity  # import first, it is a self-contained model.
from .worker import Worker as Worker
from .compensation import Compensation as Compensation

Worker.model_rebuild()
Compensation.model_rebuild()
# Optionally, you can explicitly provide the namespace to use
# to resolve missing annotations:
# Worker.model_rebuild(_types_namespace={'Compensation': Compensation})
# Compensation.model_rebuild(_types_namespace={'Worker': Worker})
