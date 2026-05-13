from pydantic import BaseModel

class WebhookResponse(BaseModel):
    message_id: str
    query_type: str
    drafted_reply: str
    confidence_score: float
    action: str