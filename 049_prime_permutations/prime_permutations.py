import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import *
from itertools import permutations
from itertools import combinations_with_replacement


def isPerm( num1, num2 ):
    return sorted( str( num1 ) ) == sorted( str( num2 ) )


def findTriplet():

    for comb in range( 1000, 10000 ):
        perms = list( permutations( str( comb ) ) )
        for i1 in range( len( perms ) ):
            num1 = int( "".join( perms[i1] ) )
            if not isPrime( num1 ) or num1 < 1000:
                continue
            for i2 in range( i1 + 1, len( perms ) ):
                num2 = int( "".join( perms[i2] ) )
                if not isPrime( num2 ) or num1 == num2 or num2 < 1000:
                    continue
                num3 = ( num2- num1 ) + num2
                if isPerm( num1, num3 ) and isPrime( num3 ):
                    if num1 not in (1487, 4817, 8147):
                        return num1, num2, num3


def main():
    print( findTriplet() )


main()
