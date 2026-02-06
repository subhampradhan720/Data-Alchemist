import json


def load_data():
    with open("data/conversations.json") as f:
        return json.load(f)


def retrieve_conversations(event):
    data = load_data()
    return [c for c in data if c["outcome"] == event]
