counts = {
    1  : 3,
    2  : 3,
    3  : 5,
    4  : 4,
    5  : 4,
    6  : 3,
    7  : 5,
    8  : 5,
    9  : 4,
    10 : 3,
    11 : 6,
    12 : 6,
    13 : 8,
    14 : 8,
    15 : 7,
    16 : 7,
    17 : 9,
    18 : 8,
    19 : 8,
    20 : 6,
    30 : 6,
    40 : 5,
    50 : 5,
    60 : 5,
    70 : 7,
    80 : 6,
    90 : 6,
}

def length( num ):
    if num > 999:
        return 11
    elif num > 99:
        if str( num )[1:] == "00":
            return counts[ int( str( num )[0] ) ] + 7   # 7 for "hundred"
        else:
            return counts[ int( str( num )[0] ) ] + 10 + length( int( str( num )[1:] ) )    # 10 for "hundred and"
    elif num > 19:
        return counts[ int( str( num )[0] + "0" ) ] + length( int( str( num )[1] ) )
    elif num == 0:
        return 0
    else:
        return counts[ num ]


count = 0
for i in range( 1, 1001 ):
    # print( i, length( i ) )
    count += length( i )
print( count )
