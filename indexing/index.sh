python -m pyserini.index.lucene \
  --collection JsonCollection \
  --input ../data/scifact/converted/corpus \
  --index ../data/scifact/indexes/scifact_collection_jsonl \
  --generator DefaultLuceneDocumentGenerator \
  --threads 1 \
  --storePositions --storeDocvectors --storeRaw
