from os.path import dirname
import os, sys
sys.path.append(dirname(dirname(dirname(os.path.abspath(__file__)))))

from util import *


def main():
    upper = 15 * (10 ** 5) + 1
    # upper = 100
    trips = generatePythagoreanPrimitives(upper)
    primitives = [0 for _ in range(upper)]
    for t in trips:
        primitives[sum(t)] += 1
    counts = [i for i in primitives]
    numSingles = 0
    for tripSum in range(len(primitives)):
        if primitives[tripSum]:
            tempTripSum = tripSum * 2
            while tempTripSum < len(counts):
                counts[tempTripSum] += 1
                tempTripSum += tripSum
    for count in counts:
        if count == 1:
            numSingles += 1            
    print(numSingles)
    


main()
