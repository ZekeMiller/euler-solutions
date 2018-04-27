import math

def findATriplet( val ):
    upper = val // 2
    for a in range( upper ):
        for b in range( a, upper ):
            c = math.sqrt( a**2 + b**2 )
            if c == int(c):
                c = int(c)
                # print( a, b, c )
                # print( a + b + c )
                if a + b + c == val:
                    return a, b, c
    return 0,0,0

a, b, c = findATriplet( 1000 )
print( a * b * c )
