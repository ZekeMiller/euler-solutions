import math


def isPrime( num ):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % ( i + 2 ) == 0:
            return False
        i += 6
    return True


def findMinOddComp():
    num = 3
    while True:
        for root in range( int( ( math.sqrt( num ) ) ) ):
            diff = num - ( 2 * root * root )
            if isPrime( diff ):
                break
        else:
            return num
        num += 2


def main():
    print( findMinOddComp() )


main()
