import json
import csv

with open("data/scifact_dev.csv", "w", newline='', encoding='utf-8') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
    with open("data/data/claims_dev.jsonl", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            writer.writerow([data["id"], data["claim"]])