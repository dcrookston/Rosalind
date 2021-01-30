#Test for GC.py

import pytest
from rosalind.GC import GC

valid_output = "Rosalind_0808\n60.91954022988506"

def test_GC():
    actual_output = GC(["tests/data/GC.txt"])
    print(actual_output)
    assert(actual_output == valid_output)
