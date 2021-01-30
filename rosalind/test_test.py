import pickle
from rosalind.Gene import gene
from rosalind.fasta import generead
import pytest

def test_generead():
    fp = open("genes.p", "rb")
    pickled_genes = pickle.load(fp)
    fp.close()

    genes = generead("FASTA.txt")
    for i in zip(pickled_genes, genes):
        assert(i[0].bases == i[1].bases)

def test_generead_nofile():
    with pytest.raises(FileNotFoundError):
        generead("nonexistent.txt")
