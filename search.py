from pyserini.search.lucene import LuceneSearcher

searcher = LuceneSearcher.from_prebuilt_index('beir-v1.0.0-scifact.flat')
searcher.set_bm25(0.82, 0.68)
hits = searcher.search(r"1,000 genomes project enables mapping of genetic sequence variation consisting of rare variants with larger penetrance effects than common variants.")

for i in range(0, 10):
    print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.6f}')
    print(hits[i].lucene_document.get('raw'))