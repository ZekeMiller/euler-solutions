# 965 * 87 = 83955 is the upper bound because I understand math, I could lower it with more testing
# but the extra few thousand iterations shouldn't be intolerable
# 3456 is a reasonable lower bound I guess

import math


def divisors( val ):
    
    if val < 1:
        return val
    if val == 1:
        return [1]
    if val == 2:
        return [1,2]
    
    facts = []
    sqrt = math.sqrt( val )
    for i in range( 2, math.floor( sqrt ) + 1 ):
        if val % i == 0:
            facts += [i]
            if i ** 2 != val:
                facts += [val // i]
    return facts


def isPandigital( num ):
    return len(str(num)) == 9 and sorted( [int(i) for i in str( num )]) == [1,2,3,4,5,6,7,8,9]



def pandigitalSum():
    tot = 0
    for i in range( 3456, 83954 ):
        facts = divisors( i )
        for fact in facts:
            if isPandigital( int( str(i) + str(fact) + str(i//fact) ) ):
                tot += i
                break
    return tot


def main():
    print( pandigitalSum() )


main()
