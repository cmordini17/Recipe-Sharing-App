from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base

class RecipeTag(Base):
    __tablename__ = "recipe_tag"

    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id", ondelete="CASCADE"), primary_key=True)
    tag_name = Column(String(255), ForeignKey("tag.name", ondelete="CASCADE"), primary_key=True)

    recipe = relationship("Recipe", back_populates="tags")
    tag = relationship("Tag", back_populates="recipes")
