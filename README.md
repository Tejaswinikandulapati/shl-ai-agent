# SHL Conversational Assessment Recommender

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