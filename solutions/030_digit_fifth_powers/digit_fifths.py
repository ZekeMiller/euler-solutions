
# 6 * 9 ** 5 because 999999 > sum of fifth powers of digits, so anything 7 digits or longer will be impossible
tot = 0

for val in range( 2, 6 * 9 ** 5 ):
    if val == sum( ( int(i) ** 5 for i in str( val ) ) ):
        tot += val

print( tot )
