from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_chat():

    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Hiring Java developer"
            }
        ]
    }

    response = client.post("/chat", json=payload)

    assert response.status_code == 200