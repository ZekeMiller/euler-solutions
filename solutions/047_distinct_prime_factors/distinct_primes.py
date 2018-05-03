import math


def primeFactors( val ):
    if val <= 3:
        return [val]
    facts = []
    for prime in range( 2, int( math.sqrt( val ) ) + 1 ):
        while val % prime == 0:
            val //= prime
            facts += [prime]
    if val != 1:
        facts += [val]
    return facts


def findFour():
    start = 1
    while True:
        for i in range( 4 ):
            facts = primeFactors( start + i )
            if len( set( facts ) ) != 4:
                break
        else:
            return start
        start += 1


def main():
    print( findFour() )


main()
# print( primeFactors( 14 ) )
# print( primeFactors( 15 ) )
# print( len( set( primeFactors( 14 ) ) ) )
# print( len( set( primeFactors( 15 ) ) ) )


# for i in range( 15 ):
#     print( primeFactors( i ) )