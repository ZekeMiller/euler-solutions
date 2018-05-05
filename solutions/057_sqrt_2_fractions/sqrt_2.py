def countBigNum( upper ):

    count = 0

    num = 2
    den = 1

    for _ in range( upper ):
        bigNum = num + den
        bigDen = num
        if len( str( bigNum ) ) > len( str( bigDen ) ):
            count += 1
        # print( bigNum, "/", bigDen )
        tempNum = 2 * num + den
        tempDen = num
        num = tempNum
        den = tempDen
    return count


def main():
    n = 1000
    print( countBigNum( n ) )


main()
