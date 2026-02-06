import json
import os

DATA_PATH = "raw/data.json"
OUTPUT_DIR = "reduced"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "filtered_data.json")

TARGET_DOMAIN = "e-commerce & retail"
TARGET_INTENT = "delivery investigation"

def normalize(text):
    if not text:
        return ""
    return " ".join(text.lower().split())

def reduce_dataset():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    transcripts = data.get("transcripts", [])
    reduced = []

    for convo in transcripts:
        domain = normalize(convo.get("domain", ""))
        intent = normalize(convo.get("intent", ""))

        if domain == TARGET_DOMAIN and intent == TARGET_INTENT:
            reduced.append(convo)

    print(f"Before reduction: {len(transcripts)}")
    print(f"After reduction: {len(reduced)}")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"transcripts": reduced}, f, indent=2)

if __name__ == "__main__":
    reduce_dataset()
