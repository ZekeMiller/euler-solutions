from functools import reduce
from operator import mul


def choose( top, bottom ):
    newTop = [ i for i in range( bottom + 1, top + 1 ) ]
    newBot = [ i for i in range( 1, bottom + 1 ) ]
    return reduce( mul, newTop, 1 ) / reduce( mul, newBot, 1 )

n = 20
print( choose( 2 * n, n ) )
