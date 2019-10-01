from os.path import dirname
import os, sys
sys.path.append(dirname(dirname(dirname(os.path.abspath(__file__)))))

from util import *


# could be used for this since the numbers aren't huge, use the safer one
# since it's only slightly slower
def isSquareSmall(n):
    return int(n ** (1/2)) == n ** (1/2)

def isPythagoreanPair(a, b):
    return isSquare(a ** 2 + b ** 2)


def firstToExceedNPaths(n):
    count = 0
    a = 0
    while count < n:
        a += 1
        for bc in range(1, 2 * a):
            if isPythagoreanPair(a, bc):
                # the number of pairs b and c to add up to bc, assuming
                # our limit will be caused by reaching below 1
                # if bc = 7, we can do (1,6), (2,5), (3,4)
                # if bc = 8, we can do (1,7), (2,6), (3,5), (4,4)
                onecap = bc//2

                # the number of pairs b and c to add up to bc, assuming
                # our limit will be caused by exceeding a
                # if a = 8 and bc = 15, the only pair is (8,7)
                # if a = 9 and bc = 12, (6,6), (7,5), (8,4), (9,3)
                acap = a - (bc-1)//2

                c = min([onecap, acap])
                count += c

        # Old brute force version
        '''
        for b in range(1, a+1):
            for c in range(1, b+1):
                result = isPythagoreanPair(a,b+c)
                if result:
                    print("a b c", a,b,c, b+c)
                    count += 1
        '''
    return a

print(firstToExceedNPaths(10 ** 6))
