#A solution to the problem "Counting Point Mutations"
#http://rosalind.info/problems/hamm/

def hamm(s, t):
    mismatches = 0
    
    if (len(s) != len(t)):
        raise ValueError("Strings must be the same length.")

    for i, char in enumerate(s):
        if t[i] != char:
            mismatches += 1

    return mismatches

hamm("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT")
