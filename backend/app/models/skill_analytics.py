from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.db import Base

class SkillAnalytics(Base):
    __tablename__ = "skill_analytics"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    problem_solving_score = Column(Float, default=0.0)
    logic_score = Column(Float, default=0.0)
    code_quality_score = Column(Float, default=0.0)
    consistency_score = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="skill_analytics")
