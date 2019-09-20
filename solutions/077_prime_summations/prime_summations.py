import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from util import *

def findFirstWith(uniqueGoal, searchUntil):
    # not sure how to mathematically find a low upper bound for the arr size
    # so have the user pass us what they hope is the upper bound
    upper = searchUntil
    orderedPrimes = sievePrimes(upper)
    primes = set(orderedPrimes)
    arr = [[0 for _ in range(upper)] for _ in range(upper)]
    for i in range(2, upper):
        # count yourself as 1
        if i in primes:
            arr[i][i] += 1
        for j in range(2, i+1):
            # can't increase until j is a new prime
            if j not in primes:
                arr[i][j] += arr[i][j-1]
                continue
            # each prime is a new combination
            for p in orderedPrimes:
                if p > j:
                    break
                arr[i][j] += arr[i-p][p]
        if arr[i][i] > uniqueGoal:
            return i
        # extend past the max
        for k in range(i+1, upper):
            arr[i][k] = arr[i][i]

# print(findFirstWith(8))
print(findFirstWith(5000, 100))
