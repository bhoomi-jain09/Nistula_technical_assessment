from fastapi import APIRouter, HTTPException

from app.model.request_model import IncomingMessage
from app.model.response_model import WebhookResponse
from app.core.logger import logger
from app.service.classify_service import classify_query
from app.service.normalize_service import normalize_message
from app.service.claude_service import generate_ai_reply
from app.service.action_service import determine_action

from app.core.logger import logger

router = APIRouter()
@router.post(
    "/webhook/message",
    response_model=WebhookResponse
)
async def receive_message(data: IncomingMessage):

    try:

        logger.info("Incoming message received")

        query_type = classify_query(data.message)

        normalized_message = normalize_message(
            data,
            query_type
        )

        ai_response = await generate_ai_reply(
            normalized_message
        )

        drafted_reply = ai_response["drafted_reply"]

        confidence_score = ai_response["confidence_score"]

        action = determine_action(
            query_type,
            confidence_score
        )

        return {
            "message_id": normalized_message["message_id"],
            "query_type": query_type,
            "drafted_reply": drafted_reply,
            "confidence_score": confidence_score,
            "action": action
        }

    except Exception as e:

            logger.exception("Webhook failed")

            raise HTTPException(
                status_code=500,
                detail=str(e)
            )