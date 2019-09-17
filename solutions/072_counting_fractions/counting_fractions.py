import os, sys                                                                  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(    __file__)))))

from util import *

def count_frac(max_d):
  primes = sievePrimes(max_d+1)
  return sum([totientWithPrimes(i, primes) for i in range(2, max_d+1)])

print(count_frac(8))
print(count_frac(30))
print(count_frac(10 ** 6))

