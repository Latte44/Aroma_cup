import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "desserts.json"

def get_desserts():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        desserts = json.load(file)

    return desserts