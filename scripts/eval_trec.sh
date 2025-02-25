#!/bin/bash

python -m pyserini.eval.trec_eval -c -mrecall.100 -mmap \
   ../data/scifact/converted/scifact_qrels_trec.txt \
   ../data/scifact/results/run.scifact.bm25-default.dev.trec.txt
