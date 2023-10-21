from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, func
from sqlalchemy.sql.sqltypes import JSON

from utils.database import Base

class Explanation(Base):
    __tablename__ = "explanation"
    
    recommendationId = Column(Integer, ForeignKey("recommendation.id"), primary_key=True, nullable=False)
    success = Column(Boolean, nullable=False)
    createdAt = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, recommendationId, success):
        self.recommendationId = recommendationId
        self.success = success