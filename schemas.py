from pydantic import BaseModel
from typing import Optional


# ---- Internal Message Schemas ----

class UserSchema(BaseModel):
    id: str
    name: Optional[str] = None


class MessageSchema(BaseModel):
    text: str


class IncomingMessage(BaseModel):
    company_id: str
    channel: str
    user: UserSchema
    message: MessageSchema


# ---- External Webhook Schema (Day 11) ----

class WebhookPayload(BaseModel):
    source: str
    company_id: str
    user_id: str
    text: str

class BookingConfirmSchema(BaseModel):
    company_id: str
    slot_id: int
    user_id: str
