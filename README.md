# SHL Conversational Assessment Recommender

# SHL Conversational Assessment Recommender

AI-powered conversational recommendation system for SHL assessments using FastAPI.

## Features
- Conversational hiring assessment recommendations
- Context clarification support
- Guardrails for off-topic conversations
- Assessment comparison support
- Seniority-based recommendations
- REST API with FastAPI
- Swagger API documentation

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Pydantic
- Git & GitHub

## Project Structure

app/
├── routes/
├── services/
├── models/
├── prompts/

## Installation

```bash
pip install -r requirements.txt
## Setup

### Install dependencies

pip install -r requirements.txt

### Create catalog

python scripts/scrape_catalog.py

### Build vector index

python scripts/build_index.py

### Run server

uvicorn app.main:app --reload

### Endpoints

GET /health
POST /chat
