import json
from collections import Counter

# Path to raw dataset
DATA_PATH = "raw/data.json"

def explore_metadata():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    transcripts = data.get("transcripts", [])

    domain_counter = Counter()
    intent_counter = Counter()

    for convo in transcripts:
        domain = convo.get("domain", "UNKNOWN")
        intent = convo.get("intent", "UNKNOWN")

        domain_counter[domain] += 1
        intent_counter[intent] += 1

    print("\n===== UNIQUE DOMAINS =====")
    for domain, count in domain_counter.items():
        print(f"{domain}  -->  {count}")

    print("\n===== UNIQUE INTENTS =====")
    for intent, count in intent_counter.items():
        print(f"{intent}  -->  {count}")

    print("\n===== SUMMARY =====")
    print(f"Total conversations: {len(transcripts)}")
    print(f"Unique domains: {len(domain_counter)}")
    print(f"Unique intents: {len(intent_counter)}")


if __name__ == "__main__":
    explore_metadata()
