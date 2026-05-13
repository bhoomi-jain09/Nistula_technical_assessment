from pydantic import BaseModel
from typing import Literal

class IncomingMessage(BaseModel):
    source: Literal[
        "whatsapp",
        "booking_com",
        "airbnb",
        "instagram",
        "direct"
    ]

    guest_name: str
    message: str
    timestamp: str
    booking_ref: str
    property_id: str
    class Config:
        json_schema_extra = {
            "example": {
                "source": "whatsapp",
                "guest_name": "Rahul Sharma",
                "message": "Is the villa available from April 20 to 24?",
                "timestamp": "2026-05-05T10:30:00Z",
                "booking_ref": "NIS-2024-0891",
                "property_id": "villa-b1"
            }
        }