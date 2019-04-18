
def __old_coin_partitions( n ):
    if n < 0:
        return None
    if n < 2:
        return [ 1 for _ in range(n+1) ]

    part = [ 0 for _ in range(n) ]
    part[0] = 1
    part[1] = 1

    row = [ 1 for _ in range(n) ]

    for j in range(2, n):
        for i in range( j, n ):
            row[i] += row[i-j]
        part[j] = row[j]

    return part


def pentagonal( n ):
    return int( n * (3 * n - 1) / 2 )


def coin_partitions( mod ):
    part = [1, 1]
    tracker = 100
    while part[-1] % mod != 0:
        p = 0
        i = 0
        pent = 1
        while pent <= len(part):
            sign = -1 if i % 4 > 1 else 1
            p += sign * part[len(part)-pent]
            p %= mod
            i += 1
            k = int( -1 * ( ( i % 2 ) * 2 - 1 ) * ( i / 2 + 1 ) )
            pent = pentagonal(k)

        part.append( p )
    return len(part)


def main():
    goal = 10 ** 6
    print( coin_partitions( goal ) )


if __name__=='__main__':
    main()
