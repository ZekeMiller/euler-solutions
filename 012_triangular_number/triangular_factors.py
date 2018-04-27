import math

def factorCount( val ):

    if val <= 2:
        return val
    
    count = 0
    sqrt = math.sqrt( val )
    for i in range( 1, math.floor( sqrt ) + 1 ):
        if val % i == 0:
            count += 2
    if sqrt == int( sqrt ):
        count -= 1
    return count


def genTriangle( num ):
    return sum( [ i for i in range( num ) ] )

def search( numFactors ):
    lastAdded = 1
    current = 1
    while factorCount( current ) < numFactors:
        lastAdded += 1
        current += lastAdded
    return current


# for k in range( 15 ):
    # print( k, factorCount( k ) )

n = 500
print( search( 500 ) )

