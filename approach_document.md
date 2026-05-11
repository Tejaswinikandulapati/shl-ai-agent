# Approach Document

## Architecture

FastAPI backend with FAISS semantic retrieval and LLM-powered conversational flow.

## Retrieval

Used sentence-transformers embeddings with FAISS vector search.

## Guardrails

Implemented keyword-based protection against prompt injection and off-topic queries.

## Recommendation Pipeline

Conversation understanding → retrieval → ranking → structured response.

## Evaluation

Tested clarification, recommendation, comparison, and refusal flows.