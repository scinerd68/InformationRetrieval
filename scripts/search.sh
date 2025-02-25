#!/bin/bash

python -m pyserini.search.lucene \
 --threads 4 --batch-size 16 \
 --index beir-v1.0.0-scifact.flat \
 --topics ../data/scifact/converted/claims_dev.tsv \
 --topics-format default \
 --output ../data/scifact/results/run.scifact.bm25-default.dev.msmarco.txt \
 --hits 100 --bm25 --k1 0.82 --b 0.68 \
 --output-format msmarco
