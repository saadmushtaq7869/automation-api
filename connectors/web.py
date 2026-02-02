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


@router.post("/web")
def web_message(payload: dict, db: Session = Depends(get_db)):
    reply = process_message(
        db=db,
        company_id=payload["company_id"],
        user_id=payload["user_id"],
        text=payload["text"]
    )

    return {"reply": reply}
