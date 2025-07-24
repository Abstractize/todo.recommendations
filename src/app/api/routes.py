from fastapi import APIRouter, Depends, Response
from fastapi.params import Body, Path
from typing import Annotated, Any, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.session import get_db
from ..auth.dependecies import get_current_user

from ..models.used import Used
from ..models.task_suggestion import TaskSuggestion

from ..services.recommendation_service import (
    get_task_recommendations,
    mark_recommendation_as_used,
)

router = APIRouter()


@router.get("", response_model=List[TaskSuggestion])
async def read_recommendations(
    token: dict[str, Any] = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> List[TaskSuggestion]:
    user_id: UUID = UUID(token["sub"])
    if not user_id:
        raise HTTPException(status_code=401, detail="No user identifier found in token")
    return await get_task_recommendations(user_id, db)


@router.patch("/{recommendation_id}/use", response_model=TaskSuggestion)
async def use_recommendation(
    recommendation_id: Annotated[UUID, Path(...)],
    used: Annotated[Used, Body(...)],
    token: dict[str, Any] = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Response:
    user_id: UUID = UUID(token["sub"])
    if not user_id:
        raise HTTPException(status_code=401, detail="No user identifier found in token")

    await mark_recommendation_as_used(recommendation_id, user_id, used.used, db)
    return Response(status_code=200)
