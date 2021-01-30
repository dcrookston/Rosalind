#A solution to "Finding a Motif in DNA"
#http://rosalind.info/problems/subs/

import re

def subs(s, t):
    start = 0
    matches = ""
    match = re.search(s, t)
    while(match is not None):
        start += match.start() + 1
        matches += str(start) + " "
        match = re.search(s, t[start:])
    return matches.rstrip()
