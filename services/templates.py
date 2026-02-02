TEMPLATES = {
    "booking_start": "📅 Sure! Please choose a time slot.",
    "booking_confirmed": "✅ Your booking is confirmed.",
    "sales_lead": "💬 Thanks for your interest! Can I know your requirement?",
    "sales_pitch": "🔥 Here is our best offer for you.",
    "support_reply": "🛠️ Our support team is checking your issue.",
    "complaint_reply": "⚠️ Sorry for the inconvenience. We are reviewing your complaint.",
    "fallback": "🤖 Sorry, I didn’t understand that."
}


def get_template(company_id: str, key: str) -> str:
    return TEMPLATES.get(key, TEMPLATES["fallback"])
