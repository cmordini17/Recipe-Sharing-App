from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredient"

    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id", ondelete="CASCADE"), primary_key=True)
    ingredient_name = Column(String(255), ForeignKey("ingredient.name", ondelete="CASCADE"), primary_key=True)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")
