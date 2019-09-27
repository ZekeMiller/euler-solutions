
class Vertex:
    def __init__(self, val, max_neighbors):
        self.val = val
        self.neighbors = [False for _ in range(max_neighbors)]
        self.active = False

    def __str__(self):
        return f'{self.val} {self.active} {self.neighbors}'

    def copy(self):
        other = Vertex(self.val, len(self.neighbors))
        other.neighbors = self.neighbors[:]
        other.active = self.active
        return other


    def __set_neighbor(self, neigh, val):
        if 0 <= neigh < len(self.neighbors):
            self.neighbors[neigh] = val
            return True
        return False

    def add_neighbor(self, neigh):
        self.active = True
        return self.__set_neighbor(neigh, True)
    
    def remove_neighbor(self, neigh):
        return self.__set_neighbor(neigh, False)

    def get_neighbor(self, neigh):
        if 0 <= neigh < len(self.neighbors):
            return self.neighbors[neigh]
        return None

class NoRepeat10Graph:

    def __init__(self):
        self.vertices = [Vertex(i, 10) for i in range(10)]

    def __str__(self):
        return '\n'.join([str(v) for v in self.vertices])

    def copy(self):
        other = NoRepeat10Graph()
        other.vertices = [self.vertices[i].copy() for i in range(10)]
        return other

    def add_edge(self, src, dest):
        if 0 <= src < len(self.vertices):
            if self.vertices[src].add_neighbor(dest):
                self.vertices[dest].active = True
                return True
        return False

    def remove_edge(self, src, dest):
        if 0 <= src < len(self.vertices):
            self.vertices[src].remove_neighbor(dest)
            return True
        return False

    def has_edge(self, src, dest):
        if src >= len(self.vertices) or dest >= len(self.vertices):
            return False
        return self.vertices[src].get_neighbor(dest)

    def find_minimal_start(self):
        minDest = None
        for dest in range(len(self.vertices)):
            if not self.vertices[dest].active:
                continue
            for src in range(len(self.vertices)):
                if self.vertices[src].get_neighbor(dest):
                    break
            else:
                if minDest is None or dest < minDest:
                    minDest = dest
        return minDest

    def remove(self, node):
        for other in range(len(self.vertices)):
            self.vertices[other].remove_neighbor(node)
            self.vertices[node].remove_neighbor(other)
        self.vertices[node].active = False


    def __solution(self):
        s = ""
        start = self.find_minimal_start()
        counter = 0
        while start is not None and counter < 10:
            self.remove(start)
            s += str(start)
            start = self.find_minimal_start()
            counter += 1
        return s

    def solution(self):
        copy = self.copy()
        return copy.__solution()


def get_input():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append( [ int(c) for c in input() ] )
    return lst


def remove_duplicates( data ):
    copy = []
    for d in data:
        if d not in copy:
            copy.append( d )
    return copy



def crack( data ):
    data = remove_duplicates( data )
    if len(data) == 0:
        return []
    g = NoRepeat10Graph()
    while len(data) > 1:
        curr = data.pop()
        g.add_edge(curr[0], curr[1])
        g.add_edge(curr[1], curr[2])
        # g.add_edge(curr[0], curr[2])
    print(str(g))
    return g.solution()



def main():
    lst = get_input()
    print(lst)
    result = crack( lst )
    print( result )


if __name__=='__main__':
    main()

