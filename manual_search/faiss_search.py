# # https://github.com/castorini/pyserini/blob/master/docs/usage-search.md

from pyserini.search.faiss import FaissSearcher
from pyserini.encode import DprQueryEncoder


encoder = DprQueryEncoder('BAAI/bge-base-en-v1.5', device='cpu')
searcher = FaissSearcher.from_prebuilt_index(
    'beir-v1.0.0-scifact.bge-base-en-v1.5',
    encoder
)

hits = searcher.search(r"1,000 genomes project enables mapping of genetic sequence variation consisting of rare variants with larger penetrance effects than common variants.")

for i in range(0, 10):
    print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.5f}')
