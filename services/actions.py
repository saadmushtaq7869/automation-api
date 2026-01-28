def execute_action(intent: str, company_id: str, channel: str):
    if intent == "sales":
        return {"reply": "Sales team will contact you soon"}

    if intent == "support":
        return {"reply": "Support team will assist you"}

    if intent == "booking":
        return {"reply": "Booking request received"}

    return {"reply": "Sorry, I did not understand your request"}
