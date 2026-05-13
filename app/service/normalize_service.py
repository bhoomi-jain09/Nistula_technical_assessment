from uuid import uuid4

def normalize_message(data, query_type):

    return {
        "message_id": str(uuid4()),
        "source": data.source,
        "guest_name": data.guest_name,
        "message_text": data.message,
        "timestamp": data.timestamp,
        "booking_ref": data.booking_ref,
        "property_id": data.property_id,
        "query_type": query_type
    }