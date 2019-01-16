import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *


def findMaxConsecutive( upper ):

    primes = genPrimes( upper )
    # print( primes )
    primeSet = set( primes )
    maxSpan = 0
    maximum = 0

    for i in range( len( primes ) ):
        for i2 in range( i + maxSpan, len( primes ) ):
            sumPrime = sum( primes[i : i + i2] )
            if sumPrime > upper:
                break
            if sumPrime in primeSet:
                maxSpan = i2
                maximum = sumPrime
    return maximum


def main():
    n = 1000000
    print( findMaxConsecutive( n ) )


main()
