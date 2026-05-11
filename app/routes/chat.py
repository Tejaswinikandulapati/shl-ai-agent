from fastapi import APIRouter

from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    messages = request.messages
    latest_message = messages[-1].content.lower()

    # EMPTY MESSAGE CHECK
    if not latest_message.strip():
        return {
            "reply": "Please provide a valid hiring request.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # MAX TURN LIMIT CHECK
    if len(messages) > 8:
        return {
            "reply": "Conversation limit reached.",
            "recommendations": [],
            "end_of_conversation": True
        }

    # OFF-TOPIC / FORBIDDEN CHECK
    forbidden_keywords = [
        "stock",
        "market",
        "crypto",
        "bitcoin",
        "movie",
        "movies",
        "sports",
        "weather",
        "politics",
        "news",
        "cricket",
        "music"
    ]

    if any(word in latest_message for word in forbidden_keywords):
        return {
            "reply": "I can only discuss SHL assessments and hiring assessment recommendations.",
            "recommendations": [],
            "end_of_conversation": True
        }

    # COMPARISON SUPPORT
    if "difference" in latest_message or "compare" in latest_message:
        return {
            "reply": (
                "OPQ32r measures personality and behavioral preferences, "
                "while General Ability Test measures cognitive and problem-solving ability."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # CLARIFICATION CHECK
    has_context = any(
        word in latest_message
        for word in ["junior", "mid", "senior", "experience", "years"]
    )

    if not has_context:
        return {
            "reply": "Sure. What is the seniority level and experience required for this role?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # RECOMMENDATION LOGIC
    recommendations = []

    if "python" in latest_message:
        recommendations.append({
            "name": "Python New",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
            "test_type": "Technical"
        })

    if "java" in latest_message:
        recommendations.append({
            "name": "Java 8 (New)",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/java-8-new/",
            "test_type": "Technical"
        })

    if "developer" in latest_message:
        recommendations.append({
            "name": "General Ability Test",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/general-ability-test/",
            "test_type": "Cognitive"
        })

    # REFINEMENT SUPPORT
    if "personality" in latest_message:
        recommendations.append({
            "name": "OPQ32r",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/opq32r/",
            "test_type": "Personality"
        })

    # FALLBACK
    if not recommendations:
        recommendations.append({
            "name": "General Technical Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/",
            "test_type": "Technical"
        })

    return {
        "reply": "Here are recommended SHL assessments based on your hiring requirements.",
        "recommendations": recommendations,
        "end_of_conversation": True
    }