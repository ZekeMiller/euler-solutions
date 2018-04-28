from itertools import permutations


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
    for i in range( 3, max, 2 ):
        if relPrime( primes, i ):
            primes += [ i ]
    return primes


def genRotations( num ):
    results = []
    for i in range( len( str( num ) ) ):
        results += [ int( str( num )[i:] + str( num )[:i] ) ]

    return results


def countCircular( upper ):

    count = 0
    primes = set( genPrimes( upper ) )
    for prime in primes:
        for rotation in genRotations( prime ):

            if rotation not in primes:
                break
        else:
            count += 1
    return count


def main():
    print( countCircular( 1000000 ) )


main()
