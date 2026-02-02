from services.database import SessionLocal
from models import MessageTemplate

db = SessionLocal()

templates = [
    MessageTemplate(
        company_id="company_123",
        template_key="booking_slots",
        content="📅 Available slots:\n{slots}\n\nReply with slot ID to confirm."
    ),
    MessageTemplate(
        company_id="company_123",
        template_key="booking_confirmed",
        content="✅ Your booking is confirmed for {slot_time}. Thank you!"
    ),
    MessageTemplate(
        company_id="company_123",
        template_key="fallback",
        content="Sorry, I didn’t understand that. Please try again."
    ),
]

db.add_all(templates)
db.commit()
db.close()

print("Templates seeded")
