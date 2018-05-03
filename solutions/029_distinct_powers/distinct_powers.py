
thing = set()

for a in range( 2, 100 + 1 ):
    for b in range( 2, 100 + 1 ):
        thing.add( a**b )
        thing.add( b**a )

print( len( thing ) )
