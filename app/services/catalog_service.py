import json

def get_catalog():

    with open("app/data/shl_catalog.json") as f:
        catalog = json.load(f)

    return catalog