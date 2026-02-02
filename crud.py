from sqlalchemy.orm import Session
from models import BotResponse

def get_response(db: Session, company_id: str, intent: str):
    return (
        db.query(BotResponse)
        .filter(
            BotResponse.company_id == company_id,
            BotResponse.intent == intent
        )
        .first()
    )
