from src.models.settings.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func


class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    attendeeId = Column(String, ForeignKey("attendees.id"))

    def __repr__(self):
        return f"CheckIns(id={self.id}, attendeeId={self.attendeeId})"
