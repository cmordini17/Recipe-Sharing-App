from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base

class Step(Base):
    __tablename__ = "step"

    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id", ondelete="CASCADE"), primary_key=True)
    number = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)

    recipe = relationship("Recipe", back_populates="step")
