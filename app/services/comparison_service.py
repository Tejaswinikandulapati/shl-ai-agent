from app.services.catalog_service import get_catalog

catalog = get_catalog()

def compare_assessments(query):

    found = []

    for item in catalog:
        if item["name"].lower() in query.lower():
            found.append(item)

    if len(found) < 2:
        return "I could not find both assessments."

    a = found[0]
    b = found[1]

    return (
        f"{a['name']} focuses on {a['description']} "
        f"while {b['name']} focuses on {b['description']}"
    )