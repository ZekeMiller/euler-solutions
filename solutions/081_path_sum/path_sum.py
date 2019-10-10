import math

def readInputToArray():
    n = int(input())
    arr = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        line = input()
        linearr = line.split(",")
        for j in range(len(linearr)):
            arr[i][j] = int(linearr[j])
    return arr


class Vertex:
    def __init__(self, cost):
        self.cost = cost
        self.neighbors = []

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def getNeighbors(self):
        return self.neighbors

    def getCost(self):
        return self.cost

    def __str__(self):
        s = f'{self.cost} -> ('
        for n in self.neighbors:
            s += f'{n.cost} '
        if self.neighbors:
            s = s[:-1] + ")"
        else:
            s = f'{self.cost}'
        return s

    __repr__ = __str__


class Graph:
    def __init__(self, arr, start, end):
        self.vertices = {}
        self.start = start
        self.end = end
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                self.vertices[(i,j)] = Vertex(arr[i][j])

    def addVertex(self, vertex):
        self.vertices[vertex] = Vertex(0)

    def addEdge(self, start, end):
        startV = self.vertices[start]
        endV = self.vertices[end]
        startV.addNeighbor(endV)

    def shortestPath(self):
        vSet = set()
        dist = {}

        for v in self.vertices:
            vert = self.vertices[v]
            dist[vert] = math.inf
            vSet.add(vert)
        startv = self.vertices[self.start]
        dist[startv] = startv.getCost()

        while vSet:
            curr = min(vSet, key=lambda v: dist[v])
            vSet.remove(curr)

            for neighbor in curr.getNeighbors():
                alt = dist[curr] + neighbor.getCost()
                if alt < dist[neighbor]:
                    dist[neighbor] = alt

        return dist[self.vertices[self.end]]


    def __str__(self):
        s = ""
        for v in self.vertices:
            s += f'({v[0]}, {v[1]}):'
            s += self.vertices[v].__str__()
            s += "\n"
        return s


def solveRightAndDownGraph(arr):
    start = (0,0)
    end = (len(arr)-1, len(arr[-1])-1)
    graph = Graph(arr, start, end)
    for i in range(len(arr)):
        for j in range(len(arr[-1])):
            if i < end[0]:
                graph.addEdge((i,j), (i+1,j))
            if j < end[1]:
                graph.addEdge((i,j), (i,j+1))
    return graph.shortestPath()


def solveRightGraph(arr):
    start = (-1, -1)
    end = (-2, -2)
    graph = Graph(arr, start, end)
    graph.addVertex(start)
    graph.addVertex(end)
    for i in range(len(arr)):
        graph.addEdge(start, (i, 0))
        graph.addEdge((i, len(arr[i])-1), end)
        for j in range(len(arr[i])):
            if i < len(arr)-1:
                graph.addEdge((i,j), (i+1, j))
            if i > 0:
                graph.addEdge((i,j), (i-1, j))
            if j < len(arr[i])-1:
                graph.addEdge((i,j), (i,j+1))
    return graph.shortestPath()

def solveFourGraph(arr):
    start = (0,0)
    end = (len(arr)-1, len(arr[-1])-1)
    graph = Graph(arr, start, end)
    for i in range(len(arr)):
        for j in range(len(arr[-1])):
            if i < end[0]:
                graph.addEdge((i,j), (i+1,j))
            if i > 0:
                graph.addEdge((i,j), (i-1,j))
            if j < end[1]:
                graph.addEdge((i,j), (i,j+1))
            if j > 0:
                graph.addEdge((i,j), (i, j-1))
    return graph.shortestPath()


arr = readInputToArray()
# print(solveRightAndDownGraph(arr))
# print(solveRightGraph(arr))
print(solveFourGraph(arr))
