from app.services.retrieval_service import retrieve_assessments


def generate_recommendations(query):

    results = retrieve_assessments(query, top_k=5)

    recommendations = []

    for item in results:
        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["test_type"]
        })

    return recommendations