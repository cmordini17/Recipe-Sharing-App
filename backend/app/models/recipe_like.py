from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base

class RecipeLike(Base):
    __tablename__ = "recipe_like"

    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("app_user.id", ondelete="CASCADE"), primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    recipe = relationship("Recipe", back_populates="likes")
    user = relationship("AppUser", back_populates="likes")
