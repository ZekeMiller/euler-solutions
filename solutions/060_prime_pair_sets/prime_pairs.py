import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *
from itertools import permutations
from itertools import combinations_with_replacement


def permutableSet( primes , primeSet ):
    # print( primes )
    for perm in permutations( primes, 2 ):
        # print( perm )
        if int( ''.join( str(i) for i in perm ) ) not in primeSet:
        # if not isPrime( int( ''.join( str(i) for i in perm ) ) ):
            # print( False )
            return False
        # print( True )
    return True


def findMin( amount ):

    # remove 2 since it will always result in an even permutation
    primeAmount = 10 ** ( amount - 1 )
    concatAmount = 10 ** ( 2 * ( amount - 1 ) )
    # print( primeAmount, concatAmount )

    primes = checkedReadPrimes( str( primeAmount ) + "primes.txt", primeAmount )[1:]
    primeSet = set( checkedReadPrimes( str( concatAmount ) + "primes.txt", concatAmount ) )

    # first iteration is just all the primes since they all permute alone
    previous = list( map( lambda thing: [thing], primes ) )

    for subInterval in range( amount - 1 ):

        current = []
        # print( previous )

        for prevSet in previous:
            for prime in primes:
                if prime < prevSet[-1]:
                    continue

                if subInterval > 2:
                    # print( prevSet + [ prime ] )
                    pass
                if permutableSet( prevSet + [ prime ] , primeSet ):
                    current += [ prevSet + [ prime ] ]
                    # print( "Permutable:", [ prevSet + [ prime ] ] )
        previous = current


    # store a list of valid configurations from previous iteration
    # for each prime
        # check if that prime added with each of the previous sets is permutable
            # if so, add it to a new list

    return previous


def main():
    amount = 5
    result = findMin( amount )

    print( min( map( sum, result ) ) )


main()
