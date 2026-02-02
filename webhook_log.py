from sqlalchemy import Column, Integer, String, JSON
from services.database import Base

class WebhookLog(Base):
    __tablename__ = "webhook_logs"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(String)
    payload = Column(JSON)
    status = Column(String)
    attempts = Column(Integer)
