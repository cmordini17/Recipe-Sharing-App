from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base

class Tag(Base):
    __tablename__ = "tag"

    name = Column(String(255), primary_key=True)

    recipes = relationship("RecipeTag", back_populates="tag")