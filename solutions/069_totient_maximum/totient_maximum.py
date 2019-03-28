import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(    __file__)))))
from util import *


def totient( n, primes ):
    factors = primeFactorsWithPrimes( n, primes )
    unique_factors = []
    for fac in factors:
        if fac not in unique_factors:
            unique_factors.append( fac )
    result = n
    for fac in unique_factors:
        result *= 1 - ( 1 / fac )
    return int( result )


def totient_max( n ):
    primes = sievePrimes( n )
    totients = [ totient( i, primes ) for i in range( 2, n + 1 ) ]
    adjusted = [ (i+2) / totients[i] for i in range(len(totients)) ]
    return adjusted.index(max(adjusted)) + 2


print( totient_max( 1000000 ) )
