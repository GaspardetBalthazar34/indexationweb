import json

def save_index(index_data, filename):
    """Sauvegarde un index dans un fichier JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=4, ensure_ascii=False)

def load_index(filename):
    """Charge un index à partir d'un fichier JSON."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)