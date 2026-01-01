import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_journals():
    path = BASE_DIR / "data" / "journals.jsonl"
    journals = {}
    with open(path, "r") as f:
        for line in f:
            obj = json.loads(line)
            journals[obj["journal_id"]] = obj["text"]
    return journals


def load_runs():
    folder = BASE_DIR / "data" / "llm_runs"
    runs = {}
    for file in folder.glob("*.json"):
        with open(file, "r") as f:
            data = json.load(f)
        jid = data["journal_id"]
        runs.setdefault(jid, []).append(data)
    return runs
