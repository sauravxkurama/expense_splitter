import json

DATA_FILE = "data.json"

def save_data(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f)

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
 