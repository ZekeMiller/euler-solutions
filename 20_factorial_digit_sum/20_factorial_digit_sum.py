def factorial( n, sum ):
    if n <= 0:
        return sum
    return factorial( n-1, sum * n )

print( sum( [ int(i) for i in str( factorial( 100, 1 ) ) ] ) )
