from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base

class Ingredient(Base):
    __tablename__ = "ingredient"

    name = Column(String(255), primary_key=True)

    recipes = relationship("RecipeIngredient", back_populates="ingredient")
