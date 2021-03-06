import math

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
    print( count )
    return primes


def primeFactors( val ):
    # primes = genPrimes( math.floor( math.sqrt( val ) ) )
    maxPrime = 1
    for prime in range( 2, int( math.sqrt( val ) ) ):
    # for prime in primes:
        while val % prime == 0:
            # print( val )
            val /= prime
            maxPrime = prime
    return maxPrime


# print( primeFactors( 13195 ) )
print( primeFactors( 600851475143 ) )
