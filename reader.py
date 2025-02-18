from pyserini.index.lucene import LuceneIndexReader

index_reader = LuceneIndexReader.from_prebuilt_index('beir-v1.0.0-scifact.flat')
print(index_reader.stats())