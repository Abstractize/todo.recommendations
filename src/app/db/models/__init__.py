from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .recommendation import Recommendation  # type: ignore
