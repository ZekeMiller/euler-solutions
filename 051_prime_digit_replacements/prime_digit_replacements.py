import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import *
from itertools import combinations


def replace( orig, num, indices ):
    lst = list( str( orig ) )
    for i in indices:
        lst[ i ] = str( num )

    # print( "  ", orig, ''.join( lst ) )
    return int( ''.join( lst ) )


def countReplaceable( num, primeSet ):
    maximum = 0
    associatedPrime = 0
    for repAmount in range( 1, len( str( num ) ) - 1 ):

        for indices in combinations( ( i for i in range( len( str( num ) ) ) ), repAmount ):

            count = 0

            for rep in range( 10 ):
                if rep == 0 and 0 in indices:
                    continue
                if 10 - rep + count <= maximum:
                    break
                replaced = replace( num, rep, indices )
                if replaced in primeSet:
                    count += 1

            if count > maximum:
                maximum = count
                if 0 in indices:
                    associatedPrime = replace( num, 1, indices )
                else:
                    associatedPrime = replace( num, 0, indices )

    return maximum, associatedPrime


def findFirstWith( num ):

    primes = genPrimes( 10 ** ( num - 2 ) )
    primeSet = set( primes)

    for prime in primes:
        replaceable, minPrime = countReplaceable( prime, primeSet )
        if replaceable >= num:
            return minPrime



def main():
    n = 8
    print( findFirstWith( n ) )
    # print( replace( 13, 2, [0] ) )
    # print( countReplaceable( 13 ) )


main()
