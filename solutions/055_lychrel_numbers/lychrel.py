import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *


def isLychrel( num ):

    for _ in range( 50 ):
        num = num + int( str( num )[::-1] )
        if isPalindrome( num ):
            return False

    return True


def countLychrel( upper ):
    count = 0
    for i in range( upper ):
        if isLychrel( i ):
            count += 1
    return count


def main():
    n = 10000
    print( countLychrel( n ) )


main()
