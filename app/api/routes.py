from fastapi import APIRouter, Depends
from typing import Any, List
from uuid import UUID

from ..auth.dependecies import get_current_user

from ..models.task_suggestion import TaskSuggestion
from ..services.recommendation_service import get_task_recommendations

router = APIRouter()


@router.get("", response_model=List[TaskSuggestion])
async def read_recommendations(
    token: dict[str, Any] = Depends(get_current_user),
) -> List[TaskSuggestion]:
    user_id: UUID = UUID(token["sub"])
    if not user_id:
        raise HTTPException(status_code=401, detail="No user identifier found in token")
    return await get_task_recommendations(user_id)
