#Tools to read FASTA files

import re
import fileinput
import sys
from rosalind.Gene import gene

def generead(filename):
    accumulator = []

    if (filename is None):
        print("Enter dataset (EOF to submit):")
    
    for line in fileinput.input(filename):
        line = line.strip()

        #Create a new gene
        if (re.match("^>", line) is not None):
            #Split the line at whitespace, skipping the first > character
            words = re.split("[\s]+", line[1:])

            #Create a new gene instance to hold this gene
            this_gene = gene(words[0])

            #Put it in the accumulator
            accumulator.append(this_gene)

        #Add base pairs to the gene    
        if (re.match("^[ACTGURYKMSWBDHVN-]+$", line) is not None):
            this_gene.add_bases(line)

    fileinput.close()

    return accumulator
