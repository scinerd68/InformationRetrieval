#!/bin/bash

python -m pyserini.search.lucene \
 --threads 4 --batch-size 16 \
 --index ../data/scifact/indexes/scifact_collection_jsonl \
 --topics ../data/scifact/converted/claims_dev.tsv \
 --topics-format default \
 --output ../data/scifact/results/run.scifact-selfbuilt.bm25-default.dev.trec.txt \
 --hits 100 --bm25 --k1 0.9 --b 0.4
