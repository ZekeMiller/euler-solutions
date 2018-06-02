import math


def nthSgonal( s, x ):
    n = ( math.sqrt( ( 8 * s - 16 ) * x + ( s - 4 ) ** 2 ) + ( s - 4 ) ) / ( 2 * s - 4 )
    return int( n ) if int( n ) == n else None


def removeSgonal( vals, s ):
    for val in vals:
        if nthSgonal( s, val ) is not None:
            break
    else:
        return None
    vals.remove( val )
    return vals


def spanGonals( vals ):

    for s in range( len( vals ) + 2, 2, -1 ):
        print( s )
        vals = removeSgonal( vals, s )
        if vals is None:
            return False

    return True


def isCyclic( vals ):       # assumes input is list of 4 digit values
    for i in range( len( vals ) ):
        j = ( i + 1 ) % len( vals )
        if str(vals[i])[2:] != str(vals[j])[:2]:
            return False

    return True


# print( spanGonals( [8128,2882,8281] ) )
# print( isCyclic( [8128,2882,8281] ) )
