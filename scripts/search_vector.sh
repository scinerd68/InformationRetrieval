#!/bin/bash

export INDEX_NAME="beir-v1.0.0-scifact.bge-base-en-v1.5.hnsw"
python -m pyserini.search.lucene \
 --threads 4 --batch-size 16 \
 --index $INDEX_NAME \
 --topics ../data/scifact/converted/claims_dev.tsv \
 --topics-format default \
 --output ../data/scifact/results/run.scifact.bge-base-hnsw.dev.trec.txt \
 --hits 100 \
#  --output-format msmarco
