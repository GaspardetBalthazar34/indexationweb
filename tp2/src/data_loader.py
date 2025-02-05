import json

def load_jsonl(filepath):
    """Load data from a JSONL file."""
    data = []
    with open(filepath, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data

def load_json(filepath):
    """Load data from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)
