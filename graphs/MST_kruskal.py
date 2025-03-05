class Graph:
    def __init__(self, size):
        self.size = size
        self.vertex_datax_data = [''] * size
        self.edges = []


    #add an edge between u and v with a given weight
    def addEdge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((weight, u, v))


    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data


    #if i is not its own parent, calls find recursively on its parent
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(self, parent, parent[i])


    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot   #attach smaller tree under larger tree
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self, V, edges):
        result = []     #MST
        i = 0       #edge counter
        edges = sorted(edges, key=lambda item: item[2])

        #each node starts as its own parent
        parent, rank = [], []
        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        while i < self.size:
            weight, u, v = self.edges[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                self.union(parent, rank, x, y)