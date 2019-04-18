
def count_summations( n ):
    if n < 0:
        return None
    if n < 2:
        return [ 1 for _ in range(n+1) ]

    n += 1

    part = [ 0 for _ in range(n) ]
    part[0] = 1
    part[1] = 1

    row = [ 1 for _ in range(n) ]

    for j in range(2, n):
        for i in range( j, n ):
            row[i] += row[i-j]
        part[j] = row[j]

    return part[-1]


def main():
    goal = 100
    print( count_summations( goal ) - 1 )


if __name__=='__main__':
    main()
