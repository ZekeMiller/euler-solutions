


def isPandigital( num ):
    return len(str(num)) == 9 and sorted( [int(i) for i in str( num )]) == [1,2,3,4,5,6,7,8,9]



def findMaxPanMult():
    result = 0

    for i in range( 9001, 10000 ):
        if i % 5 == 0:
            continue

        value = int( str( i ) + str( i * 2 ) )

        if isPandigital( value ):

            # we know the new result must be larger based on
            # the most significant 4 digits exclusively increasing
            result = value

    return result




def main():
    print( findMaxPanMult() )


main()
