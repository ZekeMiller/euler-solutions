from functools import reduce
from operator import mul

def genPrimes( max ):
    primes = [2]
    for i in range( 3, max, 2 ):
        if 0 not in [ i % k for k in primes ]:
            primes += [ i ]
        # for k in primes:
            # if i % k == 0:
                # print( i, k )
                # break
        # primes += [ i ]
    return primes

def lcm( vals ):
    result = genPrimes( max( vals ) )
    result.remove( 2 )
    n = 1
    while True:
        if 2 ** n not in vals:
            result += [ 2 ** ( n - 1 ) ]
            break;
        n += 1

    for res in result:
        if res ** 2 in vals:
            result.remove( res )
            result += [ res ** 2 ]
    return reduce(mul, result, 1)

vals = [ i for i in range( 1, 21 ) ]
print( lcm( vals ) )
