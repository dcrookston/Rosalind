#A solution to the problem "Computing GC Content" on Rosalind.info
#http://rosalind.info/problems/gc/

import re
import fileinput
import sys
import rosalind.Gene
import rosalind.fasta

def GC(filename):
    #A variable to hold the winner so far.
    winner = rosalind.Gene.gene("")

    return_str = ""
    
    gene_list = rosalind.fasta.generead(filename)
    
    for i in gene_list:
        if (i.percent_gc() > winner.percent_gc()):
            winner = i
    
    return_str += str(winner) + "\n"
    return_str += str(winner.percent_gc())
    
    return(return_str)

if (__name__ == "__main__"):
    if (len(sys.argv) > 1):
        print(GC(sys.argv[1]))
    else:
        print(GC(None))
