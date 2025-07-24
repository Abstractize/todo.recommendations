from datetime import datetime, timezone
from fastapi import HTTPException
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from ..models.recommendation import Recommendation


async def add_recommendations(
    db: AsyncSession, recommendations: list[Recommendation]
) -> list[Recommendation]:
    db.add_all(recommendations)
    await db.commit()
    for rec in recommendations:
        await db.refresh(rec)
    return recommendations


async def add_recommendation(db: AsyncSession, recommendation: Recommendation) -> None:
    db.add(recommendation)
    await db.commit()


async def get_active_recommendations(
    db: AsyncSession, user_id: UUID
) -> list[Recommendation]:
    result = await db.execute(
        select(Recommendation).where(
            Recommendation.user_id == user_id, Recommendation.used_at_utc == None
        )
    )
    return list(result.scalars().all())


async def update_recommendation_as_used(
    db: AsyncSession,
    recommendation_id: UUID,
    used: bool,
) -> None:

    stmt = (
        update(Recommendation)
        .where(Recommendation.id == recommendation_id)
        .values(used=used, used_at_utc=datetime.now(timezone.utc))
    )
    await db.execute(stmt)
    await db.commit()
