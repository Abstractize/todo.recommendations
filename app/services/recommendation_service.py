from typing import List
from uuid import UUID
from ..models.task_suggestion import TaskSuggestion


def get_task_recommendations(user_id: UUID) -> List[TaskSuggestion]:
    return [
        TaskSuggestion(
            title="Learn Python",
            description="Start with basic syntax and data structures.",
        ),
        TaskSuggestion(
            title="Create a personal budget",
            description="Track income and expenses for one month.",
        ),
        TaskSuggestion(
            title="Plan weekly meals",
            description="Save money and time by planning in advance.",
        ),
    ]
