import json
import csv

with open("data/scifact_qrels.txt", "w", newline='', encoding='utf-8') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
    with open("data/data/claims_dev.jsonl", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            writer.writerow([data["id"], 0, data["cited_doc_ids"][0], 1])