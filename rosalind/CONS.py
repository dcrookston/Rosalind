#A solution to the problem "Consensus and Profile"
#http://rosalind.info/problems/cons/

import rosalind.fasta
import rosalind.Gene
import sys

def CONS(filename):
    gene_list = rosalind.fasta.generead(filename)
    consensus_array = cons_genes(gene_list)
    consensus_string = make_string(consensus_array)

    return consensus_string

#This is probably a bad function name since it reminds me of cons() in Lisp
#But we'll keep it for now.
def cons_genes(gene_list):
    accumulator = []
    iterables = []

    #Turn the list of genes into a list of bases that we can zip
    for gene in gene_list:
        iterables.append(gene.bases)

    #Rotate the array of bases via zip so the columns are now rows
    for i in list(zip(*iterables)):
        #Count each base in each row and add them to our final list
        accumulator.append({
            "A": i.count("A"),
            "C": i.count("C"),
            "G": i.count("G"),
            "T": i.count("T")})

    return(accumulator)

def make_string(d):
    consensus_string = ""
    a_str = "A:"
    c_str = "C:"
    g_str = "G:"
    t_str = "T:"
    for i in d:
        a_str += " " + str(i["A"])
        c_str += " " + str(i["C"])
        g_str += " " + str(i["G"])
        t_str += " " + str(i["T"])
        
        consensus_string += max(i, key=lambda key:i[key])
    
    return(consensus_string + "\n" +
           a_str + "\n" +
           c_str + "\n" +
           g_str + "\n" +
           t_str)

if (__name__ == "__main__"):
    if (len(sys.argv) > 1):
        print(CONS(sys.argv[1]))
    else:
        print(CONS(None))
