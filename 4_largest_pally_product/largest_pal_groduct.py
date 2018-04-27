
def isPalindrome( val ):
    return str( val ) == str( val )[::-1]

def maxPally( upper ):
    pallys = []
    for i in range( upper, upper // 2, -1 ):
        for k in range( upper, upper // 2, -1 ):
            if isPalindrome( i * k ):
                pallys += [ i * k ]
    return max( pallys )

print( maxPally( 999 ) )
