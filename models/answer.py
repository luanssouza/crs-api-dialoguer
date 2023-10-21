from sqlalchemy import Boolean, Column, DateTime, Integer, SmallInteger, ForeignKey, String, func

from utils.database import Base

class Answer(Base):
    __tablename__ = "answer"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    dialogId = Column(Integer, ForeignKey("dialog.id"), nullable=False)
    ask = Column(Boolean, nullable=False)
    answer = Column(String(100))
    createdAt = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, dialogId, ask, answer):
        self.dialogId = dialogId
        self.ask = ask
        self.answer = answer