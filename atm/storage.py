import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "atm_data.json"

def load_data():
    if not DATA_FILE.exists():
        return {"users": {}, "atm_cash": 500000}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        data.setdefault("users", {})
        data.setdefault("atm_cash", 500000)
        return data
    except (OSError, json.JSONDecodeError):
        return {"users": {}, "atm_cash": 500000}

def save_data(data):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
