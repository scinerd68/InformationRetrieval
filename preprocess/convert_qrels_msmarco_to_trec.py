

with open("../data/scifact/converted/scifact_qrels_trec.txt", 'w') as fout:
    for line in open("../data/scifact/converted/scifact_qrels.txt"):
        fout.write(line.replace('\t', ' '))
