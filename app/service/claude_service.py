import json
import httpx

from app.core.config import settings
from app.prompt.claud_prompt import build_prompt
from app.context.property_context import PROPERTY_CONTEXT
async def generate_ai_reply(normalized_message):

    prompt = build_prompt(
        normalized_message,
        PROPERTY_CONTEXT
    )

    headers = {
        "x-api-key": settings.CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
        "anthropic-dangerous-direct-browser-access": "true"
    }

    payload = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 300,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    url = "https://api.anthropic.com/v1/messages"

    async with httpx.AsyncClient(timeout=30.0) as client:

        response = await client.post(
            url,
            headers=headers,
            json=payload
        )

    response.raise_for_status()

    result = response.json()

    text_output = ""

    for item in result["content"]:
        if item["type"] == "text":
            text_output += item["text"]
    print("\nCLAUDE RAW OUTPUT:")
    print(text_output)

    return json.loads(text_output)