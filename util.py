import math


"""
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *
"""


def isPerm( num1, num2 ):
    return sorted( str( num1 ) ) == sorted( str( num2 ) )


def primeFactors( val ):
    if val <= 3:
        return [val]
    facts = []
    for prime in range( 2, int( math.sqrt( val ) ) + 1 ):
        while val % prime == 0:
            val //= prime
            facts += [prime]
    if val != 1:
        facts += [val]
    return facts


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


def divisors( val ):
    
    if val < 1:
        return val
    if val == 1:
        return [1]
    if val == 2:
        return [1,2]
    
    facts = []
    sqrt = math.sqrt( val )
    for i in range( 2, math.floor( sqrt ) + 1 ):
        if val % i == 0:
            facts += [i]
            if i ** 2 != val:
                facts += [val // i]
    return facts



def relPrime( vals, check ):
    # print( vals, check )
    for val in vals:
        if check < val * val:
            return True
        if check % val == 0:
            return False
    return True


def genPrimes( max ):
    primes = [2]
    count = 2
    for i in range( 3, max, 2 ):
        if relPrime( primes, i ):
            primes += [ i ]
            count += i
    # print( count )
    return primes