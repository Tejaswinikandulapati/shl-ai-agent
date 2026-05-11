import json
import pickle
from sklearn.metrics.pairwise import cosine_similarity

with open("app/data/shl_catalog.json") as f:
    catalog = json.load(f)

with open("app/data/vectorizer.pkl", "rb") as f:
    vectorizer, vectors = pickle.load(f)

def retrieve_assessments(query, top_k=5):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(query_vector, vectors)[0]

    ranked = similarities.argsort()[::-1][:top_k]

    results = []

    for idx in ranked:
        results.append(catalog[idx])

    return results