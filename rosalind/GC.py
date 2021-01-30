#A solution to the problem "Computing GC Content" on Rosalind.info
#http://rosalind.info/problems/gc/

import re
import fileinput
import sys
import rosalind.Gene
import rosalind.fasta

#A variable to hold the winner so far.
winner = rosalind.Gene.gene("")

if (len(sys.argv) > 1):
    gene_list = rosalind.fasta.generead(sys.argv[1])
else:
    print("Enter dataset (EOF to submit):")
    gene_list = rosalind.fasta.generead(None)

for i in gene_list:
    if (i.percent_gc() > winner.percent_gc()):
        winner = i

print(winner)
print(winner.percent_gc())
