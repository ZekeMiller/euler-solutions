import math

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
    print( count )
    return primes