import math

from os.path import dirname
import os, sys
sys.path.append(dirname(dirname(dirname(os.path.abspath(__file__)))))
from util import *

def numExpressibleUnder(n):
    primes = genPrimes(math.ceil(math.sqrt(n)))
    found = set()
    amount = 0
    for primeSq in primes:
        square = primeSq ** 2
        if square >= n:
            break
        for primeCb in primes:
            cube = primeCb ** 3
            if square + cube >= n:
                break
            for primeQ in primes:
                quad = primeQ ** 4
                primeSum = square + cube + quad
                if primeSum >= n:
                    break
                elif primeSum not in found:
                    amount += 1
                    found.add(primeSum)
    return amount


def main():
    n = 50 * 10 ** 6
    amount = numExpressibleUnder(n)
    print(amount)


if __name__=='__main__':
    main()

