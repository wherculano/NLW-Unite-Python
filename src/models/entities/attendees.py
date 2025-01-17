from src.models.settings.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, func


class Attendees(Base):
    __tablename__ = "attendees"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey("events.id"), nullable=False)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"Attendees(id={self.id}, name={self.name}, email={self.email}, event_id={self.event_id})"
