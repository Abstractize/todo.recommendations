from .base.camel_model import CamelModel


class TaskSuggestion(CamelModel):
    title: str
    description: str
    score: int = 0
