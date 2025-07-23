from typing import List
from uuid import UUID
from ..models.task_suggestion import TaskSuggestion


# TODO: Implement the actual recommendation generation logic with ChatGPT or similar
def generate_recommendations(user_id: UUID, count: int = 3) -> List[TaskSuggestion]:
    ideas = [
        ("Organize workspace", "A clean desk improves focus."),
        ("Read a book", "Choose one you've been putting off."),
        ("Stretch every hour", "Small movements help health."),
    ]
    return [
        TaskSuggestion(title=title, description=desc) for title, desc in ideas[:count]
    ]
