#Tools to read FASTA files

import re
import fileinput
import sys
import Gene

def generead(file, accumulator):
    for line in fileinput.input(file):
        line = line.strip()

        #Create a new gene
        if (re.match("^>", line) is not None):
            words = re.split("[\s]+", line[1:])
            gene = Gene(words[0])
            accumulator.append(gene)
        if (re.match("^[ACTGURYKMSWBDHVN-]$", line) is not None):
            gene.add_bases(line)

    return accumulator
