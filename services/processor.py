from services.memory import get_state, save_state


def detect_intent(message: str) -> str:
    """
    Very simple rule-based intent detection.
    This is NOT AI yet — it's safe, fast, and stable.
    """
    message = message.lower()

    sales_keywords = ["buy", "price", "cost", "purchase", "sale"]
    booking_keywords = ["book", "booking", "appointment", "schedule"]
    support_keywords = ["help", "support", "issue", "problem"]
    complaint_keywords = ["complain", "complaint", "bad", "refund"]

    if any(word in message for word in sales_keywords):
        return "sales"

    if any(word in message for word in booking_keywords):
        return "booking"

    if any(word in message for word in support_keywords):
        return "support"

    if any(word in message for word in complaint_keywords):
        return "complaint"

    return "unknown"


def process_message(db, payload: dict) -> dict:
    """
    Main message processor.
    This works for ALL channels: WhatsApp, Zalo, Telegram, Web, Email, etc.
    """

    # ---- Required fields ----
    company_id = payload.get("company_id", "default_company")
    channel = payload.get("channel", "web")
    user_id = payload.get("user_id", "anonymous")
    message_text = payload.get("message", "").lower().strip()

    # ---- Load conversation state ----
    state = get_state(db, company_id, channel, user_id)

    # ---- If no state, detect intent ----
    if not state:
        intent = detect_intent(message_text)

        save_state(
            db,
            company_id=company_id,
            channel=channel,
            user_id=user_id,
            intent=intent,
            step="start",
            data={}
        )
    else:
        intent = state.intent

    # ---- Replies by intent ----
    if intent == "sales":
        reply_text = "💰 Thanks for your interest! What product are you looking to buy?"

    elif intent == "booking":
        reply_text = "📅 Sure! What date and time would you like to book?"

    elif intent == "support":
        reply_text = "🛠️ I’m here to help. Please describe your problem."

    elif intent == "complaint":
        reply_text = "⚠️ Sorry about the issue. Please tell me what went wrong."

    else:
        reply_text = (
            "❓ Sorry, I didn’t understand.\n"
            "You can say:\n"
            "- I want to buy\n"
            "- I want to book\n"
            "- I need support\n"
            "- I want to complain"
        )

    return {
        "reply": reply_text,
        "intent": intent
    }
