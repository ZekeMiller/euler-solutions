from itertools import combinations_with_replacement

def _fact( n, total ):
    if n < 2:
        return total
    return _fact( n - 1, total * n )


def factorial( n ):
    return _fact( n, 1 )


def findDigitFactsNaive( upper ):
    total = 0
    # skip 1 and 2
    for val in range( 3, upper ):
        if sum( [ factorial( int( i ) ) for i in str( val ) ] ) == val:
            total += val
    return total


def findDigitFactsComb( upper ):
    nums = [ i for i in range(10 ) ]
    facts = [ factorial(i) for i in nums ]
    total = 0

    # n is number of digits, no single digit combos work
    for n in range( 2, upper ):
        combinations = combinations_with_replacement( nums, n )
        # print( list( combinations ) )
        for comb in list( combinations ):
            factSum = sum( facts[i] for i in comb )
            # num digits in sum matches num digits in comb
            if len( str( factSum ) ) == n:
                # actual digits match
                if sorted( comb ) == sorted( int( i ) for i in str( factSum ) ):
                    total += factSum
    return total




def main():
    # print( findDigitFactsNaive( 40730 ) )
    print( findDigitFactsComb( 6 ) )


main()
