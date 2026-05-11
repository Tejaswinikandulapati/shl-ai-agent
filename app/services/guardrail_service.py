FORBIDDEN_TOPICS = [
    "salary",
    "legal",
    "politics",
    "hack"
]

def is_forbidden(text):

    text = text.lower()

    for topic in FORBIDDEN_TOPICS:
        if topic in text:
            return True

    return False