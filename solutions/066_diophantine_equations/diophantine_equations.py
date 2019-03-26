import math


def root_frac( radicand ):
    vals = []
    root = math.sqrt( radicand )
    a = int(root)
    start = a
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
            new_vals = []
            for val_set in vals:
                new_vals.append( val_set[0] )
            return start, new_vals
        vals.append( new_set )


def diophantine( n ):
    root = math.sqrt(n)
    if int(root) == root:
        return None

    # print( "dio:", n )
    start, lst = root_frac( n )
    # print( "period:", start, lst )
    prev_n = 0
    prev_d = 1
    num = 1
    den = 0

    x = start
    prev_n, num = num, num * x + prev_n
    prev_d, den = den, den * x + prev_d
    # print( "num, den:", prev_n, prev_d )

    i = 0
    while True:
        # print( "num, den:", num, den )
        # input( "step:" )
        if ( num * num ) - ( n * den * den ) == 1:
            return num, den
        x = lst[i]
        i = ( i + 1 ) % len(lst)
        prev_n, num = num, num * x + prev_n
        prev_d, den = den, den * x + prev_d


def solve_y( d, x ):
    # print( d, x )
    sq = ( x * x - 1 ) / d
    if sq < 0:
        return None
    result = math.sqrt( sq )
    if result > 0 and int(result) == result:
        return int(result)


def minimal_sol( d ):
    # print( d )
    root = math.sqrt( d )
    if int(root) == root:
       return None
    x = 1
    while True:
       y = solve_y( d, x )
       if y is not None:
           return x, y
       x += 1


def maximize_x( max_d ):
    best = -1
    best_d = -1
    for d in range( max_d + 1 ):
        # result = minimal_sol( d )
        result = diophantine( d )
        if result is not None:
            # print( "result", d, result )
            x,y = result
            if x > best:
                best = x
                best_d = d
    return best_d


print( maximize_x( 1000 ) )
# print( diophantine( 7 ) )
