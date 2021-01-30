#A solution to the problem "Consensus and Profile"
#http://rosalind.info/problems/cons/

import pprint

def cons(*iterables):
    accumulator = []
    for i in list(zip(*iterables)):
        accumulator.append({
            "A": i.count("A"),
            "C": i.count("C"),
            "G": i.count("G"),
            "T": i.count("T")})

    return(accumulator)

def print_cons(d):
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
    
    print(consensus_string)
    print(a_str)
    print(c_str)
    print(g_str)
    print(t_str)
