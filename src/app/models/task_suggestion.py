from uuid import UUID

from .base.camel_model import CamelModel


class TaskSuggestion(CamelModel):
    id: UUID | None = None
    title: str
    description: str
    score: int = 0
