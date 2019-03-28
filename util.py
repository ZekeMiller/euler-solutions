import math
import os
import sys


"""
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "file.txt"
abs_file_path = os.path.join(script_dir, rel_path)
"""


def isPalindrome( num ):
    return str(num) == str(num)[::-1]


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


def primeFactorsWithPrimes( val, primes ):
    if val <= 3:
        return [val]
    facts = []
    for prime in primes:
        if prime > math.sqrt( val ) + 1:
            break
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


def sievePrimes( upper ):
    bools = [ False for _ in range( upper ) ]
    bools[0] = True
    bools[1] = True
    for i in range( 4, upper, 2 ):
        bools[ i ] = True

    for i in range( 3, upper, 2 ):
        if not bools[ i ]:
            for j in range( i * i, upper, 2 * i ):
                bools[ j ] = True

    primes = []
    for i in range( upper ):
        if not bools[ i ]:
            primes += [i]

    return primes


def savePrimes( filename, amount ):
    curr_dir = os.path.dirname(__file__)
    rel_path = "data/primes/" + filename
    abs_file_path = os.path.join(curr_dir, rel_path )
    if not ( os.path.exists( abs_file_path ) and os.path.isfile( abs_file_path ) ):
        # print( "writing", amount, "primes to", abs_file_path )
        file = open( abs_file_path, "w+" )
        # file.write( ','.join( map( str, genPrimes( amount ) ) ) )
        file.write( ','.join( map( str, sievePrimes( amount ) ) ) )
        file.close()


def readPrimes( filename ):
    curr_dir = os.path.dirname(__file__)
    rel_path = "data/primes/" + filename
    abs_file_path = os.path.join(curr_dir, rel_path )
    if os.path.exists( abs_file_path ) and os.path.isfile( abs_file_path ):
        # print( "reading from", abs_file_path )
        file = open( abs_file_path )
        lst = file.readline().strip().split(",")
        file.close()
        return list( map( int, lst ) )


def checkedReadPrimes( filename, amount ):
    savePrimes( filename, amount )  # save does nothing if file exists
    return readPrimes( filename )
