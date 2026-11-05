import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "basket.json"


def get_basket():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        basket = json.load(file)

    return basket