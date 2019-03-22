
def e_func():
    # yield 2
    k = 1
    while True:
        yield 1
        yield 2 * k
        yield 1
        k += 1


def sqrt2():
    while True:
        yield 2

def nth_convergent( start, val_func, n ):
    prev_n = start
    prev_d = 1
    x = next(val_func)
    num = prev_n * x + 1
    den = x

    for i in range(n-2):
        x = next(val_func)
        prev_n, num = num, num * x + prev_n
        prev_d, den = den, den * x + prev_d
    return num, den


def sum_convergent( start, func, n ):
    n, d = nth_convergent( start, func(), n )
    # print( n, d )
    return sum( [ int(i) for i in str(n) ] )


# print( sum_convergent( 2, e_func, 10 ) )
print( sum_convergent( 2, e_func, 100 ) )

