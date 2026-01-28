from fastapi import FastAPI
from pydantic import BaseModel

from services.intent import detect_intent
from services.actions import execute_action

app = FastAPI()


# -------- Request Schema --------
class MessageRequest(BaseModel):
    company_id: str
    channel: str
    text: str
    user_id: str


# -------- Health Check --------
@app.get("/")
def root():
    return {"status": "API running"}


# -------- Main Automation Endpoint --------
@app.post("/message")
def handle_message(request: MessageRequest):
    # 1. Detect intent
    intent = detect_intent(request.text)

    # 2. Execute action based on intent
    action_result = execute_action(
        intent=intent,
        company_id=request.company_id,
        channel=request.channel
    )

    # 3. Return response
    return {
        "company_id": request.company_id,
        "user_id": request.user_id,
        "intent": intent,
        "result": action_result
    }
