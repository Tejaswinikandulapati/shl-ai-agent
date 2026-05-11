def detect_intent(query):
    query = query.lower()

    if "difference" in query or "compare" in query:
        return "comparison"

    if "add" in query or "also" in query:
        return "refinement"

    if len(query.split()) <= 3:
        return "clarification"

    return "recommendation"