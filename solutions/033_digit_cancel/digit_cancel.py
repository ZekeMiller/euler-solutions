def isNTCanceler( num, den ):
    if num == den or ( num % 10 == 0 and den % 10 == 0 ):
        return False

    numDig = [ int(i) for i in str( num ) ]
    denDig = [ int(i) for i in str( den ) ]

    if not ( len( numDig ) == 2 and len( denDig ) == 2 ):
        return False
    if not ( len(set(numDig)) == 2 and len(set(denDig)) == 2 ):
        return False
    if not len( set( numDig ) | set( denDig ) ) == 3:
        return False
    commonFact = ( set( numDig ) & set( denDig ) ).pop()
    
    numDig.remove( commonFact )
    denDig.remove( commonFact )

    numAfter = numDig[0]
    denAfter = denDig[0]

    if denAfter == 0:
        return False

    return num / den == numAfter / denAfter


def findDigitCancels():
    cancels = []
    for num in range( 10, 100 ):
        for den in range( num + 1, 100 ):
            if isNTCanceler( num, den ):
                cancels += [[num, den]]
    return cancels


def main():
    cancelers = findDigitCancels()
    # print( cancelers )
    newNum = 1
    newDen = 1
    for tup in cancelers:
        newNum *= tup[0]
        newDen *= tup[1]
    # print( newNum, newDen )
    # print( newNum / newDen )
    print( int( newDen / newNum ) )


main()
