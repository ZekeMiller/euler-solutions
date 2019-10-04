

def readInputToArray():
    n = int(input())
    arr = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        line = input()
        linearr = line.split(",")
        for j in range(len(linearr)):
            arr[i][j] = int(linearr[j])
    return arr


def dijkstra

arr = readInputToArray()
print(arr)

