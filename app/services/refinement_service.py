def merge_conversation(messages):
    combined = ""

    for msg in messages:
        if msg.role == "user":
            combined += msg.content + " "

    return combined