import math

def genPrimes( max ):
    primes = [2]
    for i in range( 3, max, 2 ):
        for k in primes:
            if i % k == 0:
                break
        primes += [ i ]
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


print( primeFactors( 13195 ) )
print( primeFactors( 600851475143 ) )
