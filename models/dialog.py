from sqlalchemy import Boolean, Column, DateTime, Integer, SmallInteger, String, func

from utils.database import Base

class Dialog(Base):
    __tablename__ = "dialog"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegramId = Column(Integer, nullable=False)
    age = Column(SmallInteger, nullable=False)
    authorization = Column(Boolean, nullable=False)
    isProposal = Column(Boolean, default=True)
    property = Column(String(50))
    object = Column(String(50))
    createdAt = Column(DateTime(timezone=True), default=func.now())
    updatedAt = Column(DateTime(timezone=True))

    @classmethod
    def fromdata(self, telegramId, age, authorization, isProposal):
        instance = self()
        
        instance.telegramId = telegramId
        instance.age = age
        instance.authorization = authorization
        instance.isProposal = isProposal

        return instance

    @classmethod
    def fromid(self, id):
        instance = self()
        
        instance.id = id

        return instance