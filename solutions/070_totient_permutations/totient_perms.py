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
    print( "generated" )
    totients = [ (i,totient( i, primes )) for i in range( 2, n + 1 ) ]
    perms = []
    for pair in totients:
        if isPerm( pair[0], pair[1] ):
            perms.append( pair )
    return min(perms, key=lambda x: x[0] / x[1] )[0]


print( totient_max( 10000000 ) )
