#!/bin/bash

export INDEX_NAME="beir-v1.0.0-scifact.bge-base-en-v1.5"
python -m pyserini.search.faiss \
 --threads 4 --batch-size 2 \
 --index $INDEX_NAME \
 --topics ../data/scifact/converted/claims_dev.tsv \
 --topics-format default \
 --output ../data/scifact/results/run.scifact.faiss-bge-base-en-v1.5.dev.trec.txt \
 --encoder BAAI/bge-base-en-v1.5
