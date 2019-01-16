import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *
from itertools import permutations


def isPrime( num ):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % ( i + 2 ) == 0:
            return False
        i += 6
    return True


def findMax():

    for perm in reversed( list( permutations( "12345678" ) ) ):
        num = int( ''.join( perm ) )
        if isPrime( num ):
            return num

    for perm in reversed( list( permutations( "1234567" ) ) ):
        num = int( ''.join( perm ) )
        if isPrime( num ):
            return num

    for perm in reversed( list( permutations( "1234" ) ) ):
        num = int( ''.join( perm ) )
        if isPrime( num ):
            return num


    # for num in range( 87654321, 2143, -2 ):
    #    if len( str( num ) ) in [4,7,8] and isPandigital( num ) and isPrime( num, fib ):
    #         return prime


def main():
    print( findMax() )


main()
