

def pentagonalN( n ):
    return int( n * ( 3 * n - 1 ) // 2 )


def genPentagons( n ):
    pentagons = []
    for i in range( 1 , n + 1 ):
        pentagons += [ pentagonalN( i ) ]

    return pentagons


def findMin():

    pents = genPentagons( 10000 )
    pentSet = set( pents )

    for i1 in range( len( pents ) ):
        pent1 = pents[ i1 ]
        for i2 in range( i1 + 1, len( pents ) ):
            pent2 = pents[ i2 ]
            if pent1 + pent2 in pentSet and pent2 - pent1 in pentSet:
                # the first one worked so no need to exhaustively search I guess
                print( pent1, pent2 )
                return pent2 - pent1


def main():
    print( findMin() )


main()
