import requests
from services.database import SessionLocal
from webhook_log import WebhookLog

# For now, we use a fake webhook tester
WEBHOOK_URL = ""

def send_webhook(company_id: str, payload: dict):
    db = SessionLocal()

    log = WebhookLog(
        company_id=company_id,
        payload=payload,
        status="pending",
        attempts=0
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    try:
        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            timeout=5
        )

        if response.status_code == 200:
            log.status = "success"
        else:
            log.status = "failed"

    except Exception:
        log.status = "failed"

    log.attempts += 1
    db.commit()
    db.close()
