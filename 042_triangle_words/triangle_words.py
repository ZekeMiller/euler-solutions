

def genTriangle( amount ):
    triangles = []
    for n in range( 1, amount + 1 ):
        triangles += [ sum( ( i for i in range( n ) )  ) ]
    return triangles


def stripWord( word ):
    return word[1:-1]


def letterValue( char ):
    return ord( char ) - ord( 'A' ) + 1


def wordValue( word ):
    value = 0
    for char in word:
        value += letterValue( char )
    return value


def countTriangles( filename ):

    amount = 0
    triangles = set( genTriangle( 23 ) )

    file = open( filename )
    text = file.readline()
    file.close()


    words = text.split( "," )

    for word in words:
        val = wordValue( stripWord( word ) )
        if wordValue( stripWord( word ) ) in triangles:
            amount += 1
    return amount


def main():

    import os
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "p042_words.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    print( countTriangles( abs_file_path ) )


main()