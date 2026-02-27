from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.db import Base

class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    assessment_id = Column(Integer, ForeignKey("assessments.id"))
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    final_score = Column(Float, nullable=True)
    risk_score = Column(Float, nullable=True)

    # Relationships
    user = relationship("User", back_populates="attempts")
    assessment = relationship("Assessment", back_populates="attempts")
    behavior_logs = relationship("BehaviorLog", back_populates="attempt")
