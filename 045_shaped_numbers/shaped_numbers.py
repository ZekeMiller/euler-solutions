import math


def nthPentagon( n ):
    return int ( n * ( 3 * n - 1 ) // 2 )


def isHexagonal( n ):
    triangle = ( math.sqrt( 8 * n + 1 ) - 1 ) / 2
    return triangle == int( triangle ) and int( triangle ) % 2 == 1


def findSecondTriPenHex():
    i = 166
    while True:
        if isHexagonal( nthPentagon( i ) ):
            return nthPentagon( i )
        i += 1


def main():
    print( findSecondTriPenHex() )


main()
