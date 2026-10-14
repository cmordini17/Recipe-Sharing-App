from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base

class Logger(Base):
    __tablename__ = "logger"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    user_id = Column(UUID(as_uuid=True), ForeignKey("app_user.id"))
    table_name = Column(String(255), nullable=False)
    action = Column(String(255), nullable=False)
    log_time = Column(TIMESTAMP, server_default=func.now())
