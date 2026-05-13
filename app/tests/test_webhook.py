from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_webhook():

    payload = {
        "source": "whatsapp",
        "guest_name": "Rahul Sharma",
        "message": "Is the villa available from April 20 to 24?",
        "timestamp": "2026-05-05T10:30:00Z",
        "booking_ref": "NIS-2024-0891",
        "property_id": "villa-b1"
    }

    response = client.post(
        "/webhook/message",
        json=payload
    )

    assert response.status_code == 200