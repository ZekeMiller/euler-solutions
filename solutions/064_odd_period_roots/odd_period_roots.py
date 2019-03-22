import math


def root_period( radicand ):
    vals = []
    root = math.sqrt( radicand )
    a = int(root)
    numer = 1
    sub = a

    while True:
        denom = radicand - sub * sub
        val = numer / ( root - sub )
        a = int(val)
        numer = denom // numer  # I think this always works oops lol
        sub = abs(sub - ( numer * a ))
        new_set = (a,numer,sub)
        if new_set in vals:
            return len(vals)
        vals.append( new_set )


def odd_periods( n ):
    total = 0
    for i in range(2, n+1):
        s = math.sqrt(i)
        if int(s) != s:
            period = root_period( i )
            total += period % 2
    return total

# print( root_period( 23 ) )
# print( odd_periods( 13 ) )
print( odd_periods( 10000 ) )

