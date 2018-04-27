import math



def genDivisorSum( val ):
    
    if val <= 2:
        return 1
    
    total = 1
    sqrt = math.sqrt( val )
    for i in range( 2, math.floor( sqrt ) + 1 ):
        if val % i == 0:
            total += i
            total += val // i
    if sqrt == int( sqrt ):
        total -= int( sqrt )

    return total


def genAbundants():
    abundants = []
    for i in range( 1, 28124 ):
        if genDivisorSum( i ) > i:
            abundants += [ i ]
    return abundants


def checkSumPossible( lst, val ):

    for num in lst:
        if num >= val:
            return False
        if ( val - num ) in lst:
            return True
    return False

def abundantSums( abundants ):
    total = 0
    for i in range( 28124 ):
        if not checkSumPossible( abundants, i ):
            total += i
    return total


def main():
    abund = genAbundants()
    print( abundantSums( set( abund ) ) )


main()
