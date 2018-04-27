

def genPrimes( max ):
    primes = [2]
    for i in range( 3, max, 2 ):
        for k in primes:
            if i % k == 0:
                break
        primes += [ i ]
    return primes

def multOrder( g, n ):
    i = 1
    while g ** i % n != 1:
        i += 1
    return i


def calcPeriod( val ):

    if val % 2 == 0 or val % 5 == 0:    # rel prime to 10
        return 0
    
    return multOrder( 10, val )



def periodMax( bound ):
    n = 0
    val = 0
    for i in genPrimes( bound ):
        p = calcPeriod( i )
        if p > n:
            val = i
            n = p
    return n, val


def main():
    print( periodMax( 1000 ) )


main()
