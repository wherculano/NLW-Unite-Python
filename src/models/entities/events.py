from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String


class Events(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)
    