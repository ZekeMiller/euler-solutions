import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *
from itertools import permutations
from itertools import combinations_with_replacement


def permutableSet( primes , primeSet ):
    for perm in permutations( primes, 2 ):
        if int( ''.join( str(i) for i in perm ) ) not in primeSet:
            return False
    return True


def findMin( amount ):

    # remove 2 since it will always result in an even permutation
    primeAmount = 10 ** ( amount - 1 )
    concatAmount = 10 ** ( 2 * ( amount - 1 ) )

    primes = checkedReadPrimes( str( primeAmount ) + "primes.txt", primeAmount )[1:]
    primeSet = set( checkedReadPrimes( str( concatAmount ) + "primes.txt", concatAmount ) )

    # first iteration is just all the primes since they all permute alone
    previous = list( map( lambda thing: [thing], primes ) )

    for subInterval in range( amount - 1 ):

        current = []

        for prevSet in previous:
            for prime in primes:
                if prime < prevSet[-1]:
                    continue

                if permutableSet( prevSet + [ prime ] , primeSet ):
                    current += [ prevSet + [ prime ] ]

        previous = current

    return previous


def main():
    amount = 5
    result = findMin( amount )

    print( min( map( sum, result ) ) )


main()
