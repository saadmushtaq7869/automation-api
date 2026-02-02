from services.memory import create_or_update_state, clear_state
from services.templates import get_template


def handle_action(db, company_id, channel, user_id, intent, message, state):

    if intent == "booking":
        if not state:
            create_or_update_state(db, company_id, channel, user_id, intent, "step_1")
            return get_template(company_id, "booking_start")

        if state.step == "step_1":
            create_or_update_state(db, company_id, channel, user_id, intent, "confirmed")
            return get_template(company_id, "booking_confirmed")

    if intent == "sales":
        if not state:
            create_or_update_state(db, company_id, channel, user_id, intent, "lead")
            return get_template(company_id, "sales_lead")

        if state.step == "lead":
            create_or_update_state(db, company_id, channel, user_id, intent, "interested")
            return get_template(company_id, "sales_pitch")

    if intent == "support":
        create_or_update_state(db, company_id, channel, user_id, intent, "open")
        return get_template(company_id, "support_reply")

    if intent == "complaint":
        create_or_update_state(db, company_id, channel, user_id, intent, "open")
        return get_template(company_id, "complaint_reply")

    return get_template(company_id, "fallback")
