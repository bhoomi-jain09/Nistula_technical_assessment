def determine_action(query_type, confidence_score):

    if query_type == "complaint":
        return "escalate"

    if confidence_score > 0.85:
        return "auto_send"

    if confidence_score >= 0.60:
        return "agent_review"

    return "escalate"