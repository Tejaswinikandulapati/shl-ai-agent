# SHL Conversational Assessment Recommender

AI-powered conversational recommendation system for SHL assessments using FastAPI.

---

## Features

- Conversational hiring assessment recommendations
- Context clarification support
- Guardrails for off-topic conversations
- Assessment comparison support
- Seniority-based recommendations
- REST API using FastAPI
- Swagger API documentation

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- Git & GitHub

---

## Project Structure

```text
app/
├── routes/
├── services/
├── models/
├── prompts/
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Create Catalog

```bash
python scripts/scrape_catalog.py
```

---

## Build Vector Index

```bash
python scripts/build_index.py
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /chat | Chat recommendation endpoint |

---

## Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I need a senior python developer"
    }
  ]
}
```

---

## Example Response

```json
{
  "reply": "Here are recommended SHL assessments based on your hiring requirements.",
  "recommendations": [
    {
      "name": "Python New",
      "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
      "test_type": "Technical"
    },
    {
      "name": "General Ability Test",
      "url": "https://www.shl.com/solutions/products/product-catalog/view/general-ability-test/",
      "test_type": "Cognitive"
    }
  ],
  "end_of_conversation": true
}
```

---

## Run Tests

```bash
pytest
```

---

## Author

Tejaswini
