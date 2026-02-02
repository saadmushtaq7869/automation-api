from fastapi import FastAPI, Depends
from services.database import engine, Base, get_db
from services.processor import process_message
from pydantic import BaseModel

app = FastAPI()


# ✅ CREATE TABLES ON STARTUP
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


class WebhookPayload(BaseModel):
    company_id: str
    channel: str
    user_id: str
    message: str


@app.post("/webhook")
def webhook(payload: WebhookPayload, db=Depends(get_db)):
    reply = process_message(db, payload.dict())
    return {"reply": reply}
