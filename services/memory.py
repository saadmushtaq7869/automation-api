import json
from datetime import datetime
from sqlalchemy.orm import Session
from models import ConversationState


def get_state(db: Session, company_id: str, channel: str, user_id: str):
    return (
        db.query(ConversationState)
        .filter(
            ConversationState.company_id == company_id,
            ConversationState.channel == channel,
            ConversationState.user_id == user_id
        )
        .first()
    )


def save_state(
    db: Session,
    company_id: str,
    channel: str,
    user_id: str,
    intent: str,
    step: str,
    data: dict
):
    # 🔑 Convert dict → JSON string
    data_json = json.dumps(data)

    state = get_state(db, company_id, channel, user_id)

    if state:
        state.intent = intent
        state.step = step
        state.data = data_json
        state.updated_at = datetime.utcnow()
    else:
        state = ConversationState(
            company_id=company_id,
            channel=channel,
            user_id=user_id,
            intent=intent,
            step=step,
            data=data_json,
            updated_at=datetime.utcnow()
        )
        db.add(state)

    db.commit()
    return state
