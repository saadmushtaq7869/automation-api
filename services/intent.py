def detect_intent(message: str) -> str:
    msg = message.lower()

    if "book" in msg or "appointment" in msg:
        return "booking"
    if "price" in msg or "buy" in msg:
        return "sales"
    if "problem" in msg or "help" in msg:
        return "support"
    if "complain" in msg:
        return "complaint"

    return "unknown"
