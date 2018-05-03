import math


def isPythagoreanPair( a, b, c ):
    return a ** 2 + b ** 2 == c ** 2


def countPossibilities( perimeter ):
    count = 0

    for c in range( int( perimeter // ( 1 + math.sqrt( 2 ) ) ), int ( perimeter // 2 + 1 ) ):
        legs = set()    # new set of legs for each c
        for a in range( 1, int( c // math.sqrt(2) ) ):
            b = perimeter - c - a
            if b not in legs:
                if isPythagoreanPair( a, b, c ):
                    count += 1
                    legs.add( a )
                    legs.add( b )

    return count


def maxPerimeterPossibilities( upper ):

    value = 0
    maximum = 0

    for perimeter in range( 12, upper, 2 ):
        poss = countPossibilities( perimeter )
        # print( perimeter, poss )
        if poss > maximum:
            maximum = poss
            value = perimeter

    return value


def main():
    print( maxPerimeterPossibilities( 1000 + 1 ) )



main()


