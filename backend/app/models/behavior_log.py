from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.db import Base

class BehaviorLog(Base):
    __tablename__ = "behavior_logs"

    id = Column(Integer, primary_key=True, index=True)
    attempt_id = Column(Integer, ForeignKey("attempts.id"))
    event_type = Column(String, index=True)  # tab_switch, face_missing, copy_paste
    severity_score = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationships
    attempt = relationship("Attempt", back_populates="behavior_logs")
