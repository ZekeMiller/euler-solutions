# map d(n) to [n1, n2, ..., ni]
# then at the end iterate through and if there's more than one value in the entry add the sum
# never mind I didn't realize how that worked
# just iterate through all numbers, check if they are in a list I keep, if they aren't check amicability
import math

def countAmicable( bound ):
    prev = []
    for val in range( bound ):
        if val in prev:
            continue
        other = genDivisorSum( val )
        if other == val:
            continue
        
        if genDivisorSum( other ) == val:
            prev += [val, other]
            print( "Pair:", val, other )
    return sum( prev )


def genDivisorSum( val ):
    
    if val <= 1:
        # print( val, val )
        return val
    if val == 2:
        # print( val, 3 )
        return 3
    
    total = 1
    sqrt = math.sqrt( val )
    for i in range( 2, math.floor( sqrt ) + 1 ):
        if val % i == 0:
            total += i
            total += val // i
    if sqrt == int( sqrt ):
        total -= int( sqrt )

    # print( val, total )
    return total


def main():
    print( countAmicable( 10000 ) )


main()
