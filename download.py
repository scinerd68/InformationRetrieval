from pyserini.search.lucene import LuceneSearcher
searcher = LuceneSearcher.from_prebuilt_index('beir-v1.0.0-scifact.flat')