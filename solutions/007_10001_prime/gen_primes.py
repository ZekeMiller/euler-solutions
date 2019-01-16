def relPrime( vals, check ):
    # print( vals, check )
    for val in vals:
        if check % val == 0:
            return False
    return True


def genNPrimes( max ):
    primes = [2]
    count = 1
    i = 3
    while count < max:
        if relPrime( primes, i ):
            primes += [ i ]
            count += 1
        i += 2
    return primes

print( genNPrimes( 10001 )[-1] )
