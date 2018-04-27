

def waysToMake( lst, val ):
    count = 1 if val in lst else 0
    less = [ i for i in lst if i < val ]
    
    for lessThan in less:
        count += waysToMake( [ j for j in less if j <= lessThan ] , val - lessThan )

    return count


def main():
    coins = [1,2,5,10,20,50,100,200]
    print( waysToMake( coins, 200 ) )


main()
