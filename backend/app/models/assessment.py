from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.db import Base

class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    difficulty = Column(String, index=True)  # easy, medium, hard
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    attempts = relationship("Attempt", back_populates="assessment")
