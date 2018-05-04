import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *


def findSixPerm():

    n = 3
    while True:
        for num in range( 10 ** n, int( ( 10 ** ( n + 1 ) // 6 ) ) ):
            if isPerm( num, 2 * num ):
                if isPerm( num, 3 * num ):
                    if isPerm( num, 4 * num ):
                        if isPerm( num, 5 * num ):
                            if isPerm( num, 6 * num ):
                                return num
        n += 1


def main():
    print( findSixPerm() )


main()
