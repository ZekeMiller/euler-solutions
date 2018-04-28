def isPalindrome( string ):
    return string == string[::-1]


def sumDoublePally( upper ):
    total = 0
    for i in range( upper ):
        # [2:] for cutting off 0b
        if isPalindrome( str( i ) ) and isPalindrome( bin ( i )[2:] ):
            total += i
    return total


def main():
    print( sumDoublePally( 1000000 ) )


main()
