def relprime( a, b ):
    while b != 0:
        a,b = b, a%b
    return a == 1


def count_fractions(d, lowerFrac, upperFrac):
    count = 0
    for lower in range( 1, d+1 ):
        for upper in range( 1, lower):
            if upper / lower >= upperFrac:
                break
            elif upper / lower > lowerFrac:
                if relprime(upper, lower):
                    count += 1
    return count

# print( count_fractions(8, 1/3, 1/2) )
print(count_fractions(12000, 1/3, 1/2))

