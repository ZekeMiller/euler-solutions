
hist = {}

def collatzCount( start ):
    count = 1
    n = start
    while n != 1:
        if n in hist:
            hist[start] = count + hist[n] - 1
            return count + hist[n] - 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        count += 1
    hist[start] = count
    return count


def main():
    val = 0
    biggest = 0
    n = 1000000
    for i in range( 1, n ):
        curr = collatzCount( i )
        if curr > biggest:
            biggest = curr
            val = i

    print( val )


# print( collatzCount( 13 ) )
# print( collatzCount( 40 ) )
# print( collatzCount( 40 ) )

main()
