def detect_intent(text: str) -> str:
    text = text.lower()

    if "price" in text or "cost" in text:
        return "sales"
    if "support" in text or "help" in text:
        return "support"
    if "book" in text or "appointment" in text:
        return "booking"

    return "unknown"
