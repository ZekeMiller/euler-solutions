tot = 0
for i in range( 1, ( 1001 - 1 ) // 2 + 1 ):
    tot += ( 4 * ( i ** 2 ) ) + i + 1
print( tot * 4 + 1 )
