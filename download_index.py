from pyserini.search.lucene import LuceneSearcher

# index_name = "beir-v1.0.0-scifact.flat"
index_name = "beir-v1.0.0-scifact.bge-base-en-v1.5.hnsw"
index_name = "beir-v1.0.0-scifact.contriever"
index_name = "beir-v1.0.0-scifact.bge-base-en-v1.5.flat"
searcher = LuceneSearcher.from_prebuilt_index(index_name)
