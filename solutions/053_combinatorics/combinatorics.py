

def _fact( n, tot ):
    if n < 2:
        return tot
    return _fact( n - 1, n * tot )


def factorial( n ):
    return _fact( n, 1 )


def choose( n, r ):
    return factorial( n ) / ( factorial( r ) * factorial( n - r ) )


def countExceeding( threshold, upperN ):

    count = 0
    for n in range( upperN + 1 ):
        for r in range( n // 2 + 1 ):
            nCr = choose( n, r )
            if nCr > threshold:
                if n % 2 == 0 and n / 2 == r:
                    count += 1
                else:
                    count += 2
    return count


def main():
    threshold = 1000000
    upperN = 100
    print( countExceeding( threshold, upperN ) )


main()
