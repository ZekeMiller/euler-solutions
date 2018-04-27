

def listFromFile( filename ):
    file = open( filename )
    text = file.readline()
    text = text.replace( "\"", "" )
    arr = text.split( "," )
    arr.sort()
    return arr


def nameValue( name ):

    return sum( [ ord(char) - ord('A') + 1 for char in name ] )
#    total = 0
#    for char in name:
#        total += ord(char) - ord('A')
#    return total


def countScores( arr ):
    return sum( [ (i+1) * nameValue( arr[i] ) for i in range( len( arr ) )  ] )
#    score = 0
#    for i in range( len( arr ) ):
#        score += ( ( i + 1 ) * nameValue( arr[i] ) )
#    return score


def main():
    print( nameValue( "COLIN" ) )
    arr = listFromFile( "p022_names.txt" )
    print( countScores( arr ) )


main()
