

def _fact( n, sum ):
    if n < 1:
        return sum
    return _fact( n - 1, sum * n )


def factorial( n ):
    return _fact( n, 1 )


def nthPerm( lst, perm ):
    if lst is []:
        return []
    if len( lst ) == 1 or perm == 0:
        # print( "perm =", perm, lst )
        return lst
    leng = len( lst )
    f1 = factorial( leng )
    
    if perm > f1:
        # not enough perms in existence
        return []
    
    fact = f1 // leng
    # print( perm, fact, lst, perm // fact )

    i = perm // fact

    # print( lst[i] )
    return [lst[i]] + nthPerm( lst[:i]+lst[i+1:], (perm) % fact)



def main():
    permList = nthPerm( [0,1,2,3,4,5,6,7,8,9], 1000000 - 1 )
    perm = "".join( str(x) for x in permList )
    print( perm )


main()
