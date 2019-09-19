# http://mathworld.wolfram.com/PythagoreanTriple.html
from collections import deque

def transformU( trip ):
    (a,b,c) = trip

    newA = a - 2 * b + 2 * c
    newB = 2 * a - b + 2 * c
    newC = 2 * a - 2 * b + 3 * c

    return [newA, newB, newC]

def transformA( trip ):
    (a,b,c) = trip

    newA = a + 2 * b + 2 * c
    newB = 2 * a + b + 2 * c
    newC = 2 * a + 2 * b + 3 * c

    return [newA, newB, newC]


def transformD( trip ):
    (a,b,c) = trip

    newA = -a + 2 * b + 2 * c
    newB = -2 * a + b + 2 * c
    newC = -2 * a + 2 * b + 3 * c

    return [newA, newB, newC]


def genPrimitives(upper):
    arr = [ 0 for _ in range( upper ) ]
    trips = deque()
    trips.append((3,4,5))
    while len(trips):
        trip = trips.pop()
        tripSum = sum(trip)
        if tripSum < upper:
            arr[tripSum] += 1
            trips.append(transformU(trip))
            trips.append(transformA(trip))
            trips.append(transformD(trip))
    return arr


'''
def findMax( arr ):
    curr = 0
    value = 0

    for perim in range( 12, len( arr ) ):
        count = arr[ perim ]
        for divisor in divisors( perim ):
            count += arr[ divisor ]

        if count > curr:
            curr = count
            value = perim

    return value
'''


def main():
    upper = 15 * (10 ** 5) + 1
    # upper = 100
    primitives = genPrimitives(upper)
    counts = [i for i in primitives]
    numSingles = 0
    for tripSum in range(len(primitives)):
        if primitives[tripSum]:
            # print(tripSum)
            tempTripSum = tripSum * 2
            while tempTripSum < len(counts):
                # print("loop", tempTripSum)
                counts[tempTripSum] += 1
                tempTripSum += tripSum
    for count in counts:
        if count == 1:
            numSingles += 1            
    print(numSingles)
    


main()
