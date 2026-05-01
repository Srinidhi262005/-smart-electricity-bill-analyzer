from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime


class InsightsLog(Base):
    __tablename__ = 'insights_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    suggestion = Column(String(1024), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship('User', back_populates='insights')

    def __repr__(self):
        return f"<InsightsLog(id={self.id}, user_id={self.user_id})>"
