import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "coffee.json"


def get_coffee():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        coffee = json.load(file)

    return coffee
