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


def truncatablePrimes( upper ):
    trunct = []
    primes = set( genPrimes( upper ) )
    for num in range( 10, upper ):
        for i in range( len( str( num ) ) ):
            # print( str( num )[i:] )
            if not int( str( num )[i:] ) in primes:
                break
        else:
            for i in range( 1, len( str( num ) ) ):
                if not int( str( num )[:i] ) in primes:
                    break
            else:
                trunct += [num]
    return trunct


def main():
    print( sum( truncatablePrimes( 1000000 ) ) )


main()