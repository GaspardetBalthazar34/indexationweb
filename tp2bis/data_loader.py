import json

def load_jsonl(filepath):
    """Charge un fichier JSONL et retourne une liste de dictionnaires."""
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

