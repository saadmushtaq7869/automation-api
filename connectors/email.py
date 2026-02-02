from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.database import SessionLocal
from services.processor import process_message

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/email")
def email_message(payload: dict, db: Session = Depends(get_db)):
    reply = process_message(
        db=db,
        company_id=payload["company_id"],
        user_id=payload["from_email"],  # email as user_id
        text=payload["body"]
    )

    return {
        "to": payload["from_email"],
        "reply": reply
    }
