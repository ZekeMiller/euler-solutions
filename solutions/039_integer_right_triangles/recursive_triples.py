# http://mathworld.wolfram.com/PythagoreanTriple.html

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *


def transformU( trip ):
    a = trip[0]
    b = trip[1]
    c = trip[2]

    newA = a - 2 * b + 2 * c
    newB = 2 * a - b + 2 * c
    newC = 2 * a - 2 * b + 3 * c

    return [newA, newB, newC]


def transformA( trip ):
    a = trip[0]
    b = trip[1]
    c = trip[2]

    newA = a + 2 * b + 2 * c
    newB = 2 * a + b + 2 * c
    newC = 2 * a + 2 * b + 3 * c

    return [newA, newB, newC]


def transformD( trip ):
    a = trip[0]
    b = trip[1]
    c = trip[2]

    newA = -a + 2 * b + 2 * c
    newB = -2 * a + b + 2 * c
    newC = -2 * a + 2 * b + 3 * c

    return [newA, newB, newC]


def genPrimitives( upper, arr, trip = [3,4,5] ):
    if sum( trip ) >= upper:
        return # []

    arr[ sum(trip) ] += 1 

    U = genPrimitives( upper, arr, transformU( trip ) )
    A = genPrimitives( upper, arr, transformA( trip ) )
    D = genPrimitives( upper, arr, transformD( trip ) )

    # return trip + U + A + D


def findMax( arr ):

    curr = 0
    value = 0

    for perim in range( 12, len( arr ) ):
        count = arr[ perim ]
        for divisor in divisors( perim ):
            count += arr[ divisor ]

        if count > curr:
            curr = count
            value = perim

    return value



def main():
    upper = 1000 + 1
    arr = [ 0 for _ in range( upper ) ]
    genPrimitives( upper, arr )
    print( findMax( arr ) )


main()