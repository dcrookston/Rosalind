#A solution to the problem "Computing GC Content" on Rosalind.info
#http://rosalind.info/problems/gc/

import re
import fileinput
import sys

#A class to represent a gene
class Gene:

    def __init__(self, name):
        self.name = name
        self.cgcount = 0
        self.length = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Gene named " + self.name

    def percent(self):
        if (self.length == 0):
            return 0
        return (self.cgcount / self.length) * 100

    def add_bases(self, bases):
        self.cgcount += bases.count("C")
        self.cgcount += bases.count("G")
        self.length += len(bases)

#A variable to hold the winner so far.
winner = Gene("")

#A temp variable to hold the gene currently being processed
this_gene = Gene("")

if (len(sys.argv) == 1):
    print("Enter dataset (EOF to submit):")

#Read in copy-pasted data
for line in fileinput.input():

    line = line.strip()
    #This line is a label
    if (re.match("^>[\s]*Rosalind_[\d]", line) is not None):
        #Replace old this_gene with our new gene
        this_gene = Gene(line[1:])

    #This line is a string of bases
    elif (re.match("^[ACTG]+$", line) is not None):
        #Update the gene with the current list of bases
        this_gene.add_bases(line)

    if (this_gene.percent() > winner.percent()):
        winner = this_gene

print(winner)
print(winner.percent())
