#Test for GC.py

import pytest
from rosalind.GC import GC
from rosalind.CONS import CONS

def test_GC():
    valid_output = "Rosalind_0808\n60.91954022988506"
    actual_output = GC(["tests/data/GC.txt"])
    assert(actual_output == valid_output)

def test_CONS():
    valid_output = "ATGCAACT\nA: 5 1 0 0 5 5 0 0\nC: 0 0 1 4 2 0 6 1\nG: 1 1 6 3 0 1 0 0\nT: 1 5 0 0 0 1 1 6"
    actual_output = CONS(["tests/data/CONS.txt"])
    assert(actual_output == valid_output)
