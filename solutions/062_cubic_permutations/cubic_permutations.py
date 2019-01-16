
import math


def findSmallestWithPerms( numPerms ):
    """
    finds the smallest cube with exactly numPerms amount of permutations also
    being cubes
    numPerms: must be positive integer
    return: smallest valid number
    """

    # must have at least 3 digits to get 5 permutations
    # the pattern is that the number of digits in the answer must have at least
    # enough digits to make numPerms permutations.  A number can make n! perms
    # there's no good way (that I know of at least) to do it backwards, but
    # factorials increase extremely quickly so it's safe to do it linearly
    # since it is effectively even lower time complexity than logarithmic
    # since to my understanding it would be 'inverse-factorial' time
    # then, starting from there, in order to find the smallest, we
    # iterate through cubes by number of digits (in result not root)
    # and do all of our checking there
    
    
    factN = 1
    factResult = math.factorial( factN )
    while factResult < numPerms:
        factN += 1
        factResult = math.factorial( factN )

    length = factN
    base = math.ceil( ( 10 ** length ) ** ( 1 / 3 ) )
    print( "length: ", length, " base: ", base )

    while True:
        squares = []
        while len( str( base ** 3 ) ) == length:
            squares.append( base ** 3 )
            base += 1
        print( len( squares ) )
        for val in squares:
            valSorted = ''.join( sorted( str( val ) ) )
            count = 0
            for val2 in squares:
                if valSorted == ''.join( sorted( str( val2 ) ) ):
                    count += 1
            if count == numPerms:
                return val

        length += 1


def main():
    print( findSmallestWithPerms( 5 ) )
    

if __name__ == '__main__':
    main()

