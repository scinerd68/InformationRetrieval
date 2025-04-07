# https://github.com/castorini/pyserini/blob/master/docs/usage-index.md
import json


with open("../data/scifact/converted/corpus_converted.jsonl", "w", encoding="utf-8") as outfile:
    with open("../data/scifact/download/corpus.jsonl", encoding="utf-8") as f:
        for line in f:
            document = json.loads(line)
            doc_id = document["doc_id"]
            text = document["title"] + '\n' + '\n'.join(document["abstract"])

            new_doc = {
                "id": doc_id,
                "contents": text
            }
            json.dump(new_doc, outfile)
            outfile.write('\n')
