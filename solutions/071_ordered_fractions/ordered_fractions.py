def gcd( a, b ):
    while b != 0:
        a,b = b, a%b
    return a


def ordered_frac():
    upper = 10 ** 6
    start = int( upper / 10 )
    best = (2,5)
    for lower in range( start, upper + 1 ):
        for upper in range( int( lower * best[0] / best[1] ), lower ):
            if upper / lower >= 3 / 7 :
                break
            if upper / lower >= best[0] / best[1]:
                if gcd(upper, lower) == 1:
                    best = (upper, lower)
    return best

print( ordered_frac() )

