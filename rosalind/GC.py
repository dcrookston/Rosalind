#A solution to the problem "Computing GC Content" on Rosalind.info
#http://rosalind.info/problems/gc/

import re
import fileinput
import sys
import rosalind.Gene

#A variable to hold the winner so far.
winner = Gene.gene("")

#A temp variable to hold the gene currently being processed
this_gene = Gene.gene("")

if (len(sys.argv) == 1):
    print("Enter dataset (EOF to submit):")

#Read in copy-pasted data
for line in fileinput.input():

    line = line.strip()
    #This line is a label
    if (re.match("^>[\s]*Rosalind_[\d]", line) is not None):

        if (this_gene.percent_gc() > winner.percent_gc()):
            winner = this_gene
            
        #Replace old this_gene with our new gene
        this_gene = Gene.gene(line[1:])

    #This line is a string of bases
    elif (re.match("^[ACTG]+$", line) is not None):
        #Update the gene with the current list of bases
        this_gene.add_bases(line)

if (this_gene.percent_gc() > winner.percent_gc()):
    winner = this_gene

print(winner)
print(winner.percent_gc())
