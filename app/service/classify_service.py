def classify_query(message: str) -> str:

    text = message.lower()

    if any(word in text for word in [
        "available",
        "availability",
        "dates"
    ]):
        return "pre_sales_availability"

    if any(word in text for word in [
        "rate",
        "price",
        "cost",
        "amount"
    ]):
        return "pre_sales_pricing"

    if any(word in text for word in [
        "wifi",
        "check in",
        "check-out"
    ]):
        return "post_sales_checkin"

    if any(word in text for word in [
        "airport transfer",
        "early check-in",
        "cab facility",
        "decoration",
        "pool facility"
    ]):
        return "special_request"

    if any(word in text for word in [
        "not happy",
        "issue",
        "problem",
        "not working",
        "not satisfy",
        "bad"
    ]):
        return "complaint"

    return "general_enquiry"