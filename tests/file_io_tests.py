import pytest
import pickle
from Gene import gene
from fasta import generead

class ReadFASTATest(unittest.TestCase):
    def setUp(self):
        fp = open("genes.p", "rb")
        self.pickled_genes = pickle.load(fp)
        fp.close()
    
    def test_generead(self):
        self.genes = generead("FASTA.txt")
        for i in zip(self.pickled_genes, self.genes):
            self.assertEqual(i[0].bases, i[1].bases)

    def test_readfailure2(self):
        with self.assertRaises(FileNotFoundError):
            generead("nonexistent.txt")

if __name__ == '__main__':
    unittest.main()
