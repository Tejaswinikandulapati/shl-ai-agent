from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def embed_query(query):
    return vectorizer.fit_transform([query]).toarray()