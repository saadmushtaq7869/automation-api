from services.database import companies_collection

def load_company_config(company_id: str):
    company = companies_collection.find_one(
        {"company_id": company_id},
        {"_id": 0}
    )

    if not company:
        return {
            "enabled_intents": ["sales", "support"],
            "fallback_intent": "support"
        }

    return company
