#!/bin/bash

export INDEX_NAME="beir-v1.0.0-scifact.flat"
python -m pyserini.search.lucene \
 --threads 4 --batch-size 16 \
 --index $INDEX_NAME \
 --topics ../data/scifact/converted/claims_dev.tsv \
 --topics-format default \
 --output ../data/scifact/results/run.scifact.bm25-default.dev.trec.txt \
 --hits 100 --bm25 --k1 0.9 --b 0.4 \
#  --output-format msmarco
