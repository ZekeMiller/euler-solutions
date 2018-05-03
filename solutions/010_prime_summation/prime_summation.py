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

n = 2000000
genPrimes( n )
