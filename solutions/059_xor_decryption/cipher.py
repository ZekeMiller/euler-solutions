from itertools import combinations_with_replacement
from itertools import permutations


def decryptChar( encrypted, key ):
    return encrypted ^ key


def decryptString( lst, key ):

    total = 0

    newList = [ None for _ in range( len( lst ) ) ]

    for i in range( len( lst ) ):
        newChar = chr( decryptChar( int( lst[i] ), ord( key[ i % len(key) ] ) ) )
        newList[i] = newChar
        total += ord( newChar )

    if len( list( filter( wordChar, newList ) ) ) / len( newList ) > 0.8:
        if max( [ len( word ) for word in ''.join( newList ).split( " " ) ] ) < 20:
            print( "key:", key )
            print( ''.join( newList ) )
            print( total )


def wordChar( char ):
    return char.isalpha() or char.isdigit() or ord( char ) == 32 or ord( char ) == 46


def bruteForce( filename ):

    file = open( filename )
    lst = file.readline().strip().split(",")
    file.close()

    for comb in combinations_with_replacement( 'abcdefghijklmnopqrstuvwxyz', 3 ):
        for key in permutations( comb ):
            decryptString( lst, ''.join( key ) )


def main():

    import os
    script_dir = os.path.dirname(__file__)
    rel_path = "p059_cipher.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    bruteForce( abs_file_path )


main()
