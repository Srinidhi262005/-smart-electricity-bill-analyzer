from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime


class UsageHistory(Base):
    __tablename__ = 'usage_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    units = Column(Float, nullable=False)
    predicted_bill = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship('User', back_populates='usage_records')

    def __repr__(self):
        return f"<UsageHistory(id={self.id}, user_id={self.user_id}, units={self.units})>"
