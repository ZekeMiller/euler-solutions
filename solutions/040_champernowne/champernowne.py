

def champernowne( goalIndices ):
    goalIndices.sort(reverse = True)
    upper = goalIndices[0]
    product = 1
    digits = 0
    nextGoal = goalIndices.pop()
    for i in range( 1, upper ):
        if digits > upper:
            break
        if digits + len(str(i)) >= nextGoal:
            # print( digits, i, nextGoal )
            product *= int(str(i)[ nextGoal - digits - 1 ] )
            nextGoal = goalIndices.pop()
            if len( goalIndices ) == 0:
                break
        digits += len(str(i))

    return product


def main():
    print( champernowne( [10**i for i in range( 8 ) ] ) )


main()
