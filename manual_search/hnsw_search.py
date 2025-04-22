# https://github.com/castorini/pyserini/blob/master/docs/usage-search.md

from pyserini.search.faiss import FaissSearcher
from pyserini.search.lucene import LuceneHnswDenseSearcher, LuceneSearcher

# lucene_searcher = LuceneSearcher.from_prebuilt_index('beir-v1.0.0-scifact.flat')
searcher = LuceneHnswDenseSearcher.from_prebuilt_index(
    'beir-v1.0.0-scifact.bge-base-en-v1.5.hnsw',
    ef_search=1000,
    encoder='BgeBaseEn15')

# searcher = FaissSearcher.from_prebuilt_index('beir-v1.0.0-scifact.bge-base-en-v1.5.flat')

hits = searcher.search(r"1,000 genomes project enables mapping of genetic sequence variation consisting of rare variants with larger penetrance effects than common variants.")

for i in range(0, 10):
    print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.6f}')
    # print(lucene_searcher.doc(hits[i].docid).raw())
