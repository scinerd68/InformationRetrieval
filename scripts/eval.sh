#!/bin/bash

python -m pyserini.eval.msmarco_passage_eval \
  ../data/scifact/converted/scifact_qrels.txt \
  ../data/scifact/results/run.scifact.bm25-default.dev.msmarco.txt
