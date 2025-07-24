from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone
import uuid

from . import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    score = Column(Integer, default=0)

    created_at_utc = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    created_by = Column(UUID(as_uuid=True), nullable=False)

    used = Column(Boolean, default=False, nullable=False)
    used_at_utc = Column(DateTime(timezone=True), default=None, nullable=True)
