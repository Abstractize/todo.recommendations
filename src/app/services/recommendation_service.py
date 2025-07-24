from typing import List
from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.task_suggestion import TaskSuggestion
from ..db.models.recommendation import Recommendation
from ..engines.recommendation_engine import (
    generate_recommendations,
)

from ..db.repositories.recommendation_repo import (
    add_recommendations,
    find_recommendation,
    get_active_recommendations,
    update_recommendation_as_used,
)

RECOMMENDATION_TARGET = 3


async def get_task_recommendations(
    user_id: UUID, db: AsyncSession
) -> List[TaskSuggestion]:
    existing = await get_active_recommendations(db, user_id)
    num_existing = len(existing)
    num_needed = max(RECOMMENDATION_TARGET - num_existing, 0)

    new_suggestions = []
    if num_needed > 0:
        generated = generate_recommendations(user_id, count=num_needed)
        recommendations = [
            Recommendation(
                user_id=user_id,
                title=suggestion.title,
                description=suggestion.description,
                score=suggestion.score,
                created_by=user_id,
            )
            for suggestion in generated
        ]
        saved_recommendations = await add_recommendations(db, recommendations)

        for suggestion, saved in zip(generated, saved_recommendations):
            suggestion.id = getattr(saved, "id", None)
        new_suggestions = generated

    # Convert all to TaskSuggestion
    result = [TaskSuggestion(**rec.__dict__) for rec in existing] + new_suggestions
    return result


async def mark_recommendation_as_used(
    recommendation_id: UUID,
    user_id: UUID,
    used: bool,
    db: AsyncSession,
) -> TaskSuggestion:
    recommendation: Recommendation = await find_recommendation(db, recommendation_id)

    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")

    await update_recommendation_as_used(
        db,
        used=used,
        recommendation_id=recommendation_id,
    )

    return TaskSuggestion(**recommendation.__dict__)
