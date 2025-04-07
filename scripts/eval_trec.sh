#!/bin/bash

python -m pyserini.eval.trec_eval -c -m ndcg_cut.10 -m recall.10 -m map \
   ../data/scifact/converted/scifact_qrels_trec.txt \
   ../data/scifact/results/run.scifact.bm25-default.dev.trec.txt
