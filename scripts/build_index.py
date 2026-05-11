import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

with open("app/data/shl_catalog.json") as f:
    catalog = json.load(f)

texts = []

for item in catalog:
    text = f"{item['name']} {item['description']}"
    texts.append(text)

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(texts)

with open("app/data/vectorizer.pkl", "wb") as f:
    pickle.dump((vectorizer, vectors), f)

print("Vector index built")