import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *


def upperLeft( layer ):
    return lowerRight( layer ) - ( 2 * layer * 2 )


def lowerLeft( layer ):
    return lowerRight( layer ) - ( 2 * layer * 1 )


def upperRight( layer ):
    return lowerRight( layer ) - ( 2 * layer * 3 )


def lowerRight( layer ):
    return ( 2 * layer + 1 ) ** 2


def findFirstLayerBelow( threshold ):

    primes = 0
    total = 1
    layer = 1
    while True:
        if isPrime( lowerLeft( layer ) ):
            primes += 1
        if isPrime( upperLeft( layer ) ):
            primes += 1
        if isPrime( upperRight( layer ) ):
            primes += 1
        total += 4
        if primes / total < threshold:
            return layer
        layer += 1


def main():
    threshold = 0.1
    print( 2 * findFirstLayerBelow( threshold ) + 1 )


main()
