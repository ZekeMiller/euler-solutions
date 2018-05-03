from itertools import permutations

def isSubstringDivisible( num ):

    if not int( str( num )[1:4] ) % 2 == 0:
        return False

    if not int( str( num )[2:5] ) % 3 == 0:
        return False

    if not int( str( num )[3:6] ) % 5 == 0:
        return False

    if not int( str( num )[4:7] ) % 7 == 0:
        return False

    if not int( str( num )[5:8] ) % 11 == 0:
        return False

    if not int( str( num )[6:9] ) % 13 == 0:
        return False

    if not int( str( num )[7:10] ) % 17 == 0:
        return False

    return True


def sumSubDivisible():

    total = 0

    for perm in permutations( "0123456789" ):
        num = int( ''.join( perm ) )
        if num > 1023456789 and isSubstringDivisible( num ):
            total += num

    return total


def main():
    print( sumSubDivisible() )


main()
# print( isSubstringDivisible( 1406357289 ) )
