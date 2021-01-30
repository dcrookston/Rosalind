#Tools to read FASTA files

import re
import fileinput
import sys
from Gene import gene

def generead(file):
    accumulator = []
    for line in fileinput.input(file):
        line = line.strip()

        #Create a new gene
        if (re.match("^>", line) is not None):
            words = re.split("[\s]+", line[1:])
            this_gene = gene(words[0])
            accumulator.append(this_gene)
        if (re.match("^[ACTGURYKMSWBDHVN-]+$", line) is not None):
            this_gene.add_bases(line)

    fileinput.close()

    return accumulator
