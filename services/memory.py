# services/memory.py

conversation_store = {}

def get_conversation(company_id: str, user_id: str):
    key = f"{company_id}:{user_id}"
    return conversation_store.get(key, [])

def save_message(company_id: str, user_id: str, role: str, content: str):
    key = f"{company_id}:{user_id}"

    if key not in conversation_store:
        conversation_store[key] = []

    conversation_store[key].append({
        "role": role,
        "content": content
    })

    # keep last 15 messages only
    conversation_store[key] = conversation_store[key][-15:]
