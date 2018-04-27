from functools import reduce
from operator import mul


lst = list( range( 1, 101 ) )
print( sum( lst ) ** 2 - sum( [ i ** 2 for i in lst ] ) )
