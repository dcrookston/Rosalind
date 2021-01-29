#A solution to the problem "Mendel's First Law"
#http://rosalind.info/problems/iprb/

#Calculates the probability that the offspring of two randomly selected
# members of a population will display a dominant trait. The population is
# defined by three numbers: k, m, and n.
# k is the number of homozygous dominant members
# m is the number of heterozygous members
# n is the number of homozygous recessive members

def iprb(k, m, n):
    total = k + m + n

    #We are going to calculate the probabilities for every potential combination
    # of pairings between two randomly selected parents from this population.
    # This step only tells us the probability that a particular pairing will be
    # selected, NOT the chance of that pairing producing offspring with the
    # dominant trait.
    
    #Calculate the probabilities for the first parent
    x_k = k / total
    x_m = m / total
    x_n = n / total

    #Calculate the probabilities for the second parent.

    #% for the second parent, given that the first parent is k
    xk_yk = ((k - 1) / (total - 1)) * x_k
    xk_ym = (m / (total - 1)) * x_k
    xk_yn = (n / (total - 1)) * x_k

    #% for the second parent, given that the first parent is m
    xm_yk = (k / (total - 1)) * x_m
    xm_ym = ((m - 1) / (total - 1)) * x_m
    xm_yn = (n / (total - 1)) * x_m

    #% for the second parent, given that the first parent is n
    xn_yk = (k / (total - 1)) * x_n
    xn_ym = (m / (total - 1)) * x_n
    xn_yn = ((n - 1) / (total - 1)) * x_n

    #The majority of pairings have a 100% chance to produce an offspring
    # that displays the dominant trait.  For pairings with less than 100%
    # we have to adjust the probability of the pairing by the probability
    # that their offspring will have the dominant trait.

    #m + m = 75% of getting the dominant trait
    xm_ym = xm_ym * .75

    #These two have a 50% chance each
    xm_yn = xm_yn * .5
    xn_ym = xn_ym * .5

    #n + n = 0%; we'll just leave it out of our result set

    #Now we can sum the probabilities (except n+n) for our answer
    print(xk_yk + xk_ym + xk_yn + xm_yk + xm_ym + xm_yn + xn_yk + xn_ym)
