import math


def nthSgonal( s, x ):
    n = ( math.sqrt( ( 8 * s - 16 ) * x + ( s - 4 ) ** 2 ) + ( s - 4 ) ) / ( 2 * s - 4 )
    return int( n ) if int( n ) == n else None


def isSgonal( s, x ):
    return nthSgonal( s, x ) is not None


def anyGonal( x, upper ):       # checks if x is an s-gonal for any s in [3,upper]
    for s in range( 3, upper + 1 ):
        if isSgonal( s, x ):
            # print( x, " is ", s )
            return True
    return False


def removeSgonal( vals, s ):
    for val in vals:
        if isSgonal( s, val ):
            break
    else:
        return None
    vals.remove( val )
    return vals


def spanGonals( vals ):
    for s in range( len( vals ) + 2, 2, -1 ):
        # print( s )
        vals = removeSgonal( vals[:], s )
        if vals is None:
            return False
    return True


def isCyclic( vals ):       # assumes input is list of 4 digit values
    for i in range( len( vals ) ):
        j = ( i + 1 ) % len( vals )
        if str(vals[i])[2:] != str(vals[j])[:2]:
            return False
    return True


def findNCycle( n, vals=[] ):        # finds cyclic set of length 4 ints that spans figurates from 3 up
    # print( vals )
    if len(vals) == n:
        if isCyclic( vals ) and spanGonals( vals ):
            return vals
        else:
            return None

    for val in range( 1000, 10000 ):
        if ( vals == [] or str(vals[-1])[2:] == str(val)[:2] ) and int(str(val)[2:]) >= 10 and anyGonal( val, n + 2 ):
            temp = findNCycle( n, vals + [val] )
            if temp is not None:
                return temp
    return None


# print( spanGonals( [8128,2882,8281] ) )
# print( isCyclic( [8128,2882,8281] ) )

cycle = findNCycle( 6 )
print( cycle )
print( sum( cycle ) )