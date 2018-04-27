def relPrime( vals, check ):
    # print( vals, check )
    for val in vals:
        if check % val == 0:
            return False
    return True


def genPrimes( max ):
    primes = [2]
    for i in range( 3, max, 2 ):
        if relPrime( primes, i ):
            primes += [ i ]
    return primes


def checkSeries( a, b, primeSet ):
    n = 0
    while n ** 2 + n * a + b in primeSet:
        n += 1

    return n


def quadraticMax( upper, primes, primeSet ):
    curr_n = 0
    curr_a = 0
    curr_b = 0
    
    for a in range( upper ):
        for b in primes:
            if b > 1000:
                break
            
            n = checkSeries( a, b, primeSet )
            if n > curr_n:
                curr_n = n
                curr_a = a
                curr_b = b
            n = checkSeries( -a, b, primeSet )
            if n > curr_n:
                curr_n = n
                curr_a = -a
                curr_b = b
            n = checkSeries( a, -b, primeSet )
            if n > curr_n:
                curr_n = n
                curr_a = a
                curr_b = -b
            n = checkSeries( -a, -b, primeSet )
            if n > curr_n:
                curr_n = n
                curr_a = -a
                curr_b = -b
    
    return curr_a * curr_b


def main():
    primes = genPrimes( 10000 )
    primeSet = set( primes )
    print( quadraticMax( 1000, primes, primeSet ) )


main()
