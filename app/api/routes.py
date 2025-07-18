from fastapi import APIRouter, Query
from typing import List
from uuid import UUID

from ..models.task_suggestion import TaskSuggestion
from ..services.recommendation_service import get_task_recommendations

router = APIRouter()


@router.get("", response_model=List[TaskSuggestion])
def read_recommendations(
    user_id: UUID = Query(..., alias="userId")
) -> List[TaskSuggestion]:
    return get_task_recommendations(user_id)
