import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("app/data/shl_catalog.json") as f:
    catalog = json.load(f)

texts = []

for item in catalog:
    text = f"{item['name']} {item['description']} {' '.join(item['skills'])}"
    texts.append(text)

embeddings = model.encode(texts)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, "app/data/faiss.index")

print("FAISS index built")