from fastapi import APIRouter

router = APIRouter()


@router.post("/webhook/make")
def receive_make_webhook(data: dict):
    """
    Endpoint for Make.com to send data back
    """

    return {
        "status": "received",
        "data": data
    }
