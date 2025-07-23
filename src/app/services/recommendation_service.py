from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.task_suggestion import TaskSuggestion
from ..db.models.recommendation import Recommendation
from ..engines.recommendation_engine import (
    generate_recommendations,
)

RECOMMENDATION_TARGET = 3


async def get_task_recommendations(
    user_id: UUID, db: AsyncSession
) -> List[TaskSuggestion]:

    result = await db.execute(
        select(Recommendation).where(Recommendation.user_id == user_id)
    )
    existing = result.scalars().all()

    missing = RECOMMENDATION_TARGET - len(existing)
    new_recos = []
    if missing > 0:
        new_recos = generate_recommendations(user_id, count=missing)
        for r in new_recos:
            db.add(
                Recommendation(
                    user_id=user_id,
                    title=r.title,
                    description=r.description,
                    score=r.score,
                )
            )
        await db.commit()

    existing_suggestions = [TaskSuggestion(**r.__dict__) for r in existing]
    combined = existing_suggestions + new_recos
    return combined
