from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from services.database import Base


class ConversationState(Base):
    __tablename__ = "conversation_states"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(String, index=True)
    channel = Column(String, index=True)
    user_id = Column(String, index=True)

    intent = Column(String)          # booking / sales / support / complaint
    step = Column(String)            # step_1, step_2, confirmed, closed
    data = Column(Text, nullable=True)

    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class MessageLog(Base):
    __tablename__ = "message_logs"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(String)
    channel = Column(String)
    user_id = Column(String)
    message = Column(Text)
    intent = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
