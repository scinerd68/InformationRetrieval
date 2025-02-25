import json
import csv

with open("../data/scifact/converted/claims_dev.tsv", "w", newline='', encoding='utf-8') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
    with open("../data/scifact/download/claims_dev.jsonl", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            writer.writerow([data["id"], data["claim"]])
