import heapq


class Graph:
    def __init__(self, size):
        self.adj_list = {i: [] for i in range(size)}
        self.size = size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))    #remove for directed graph
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    # O(|V|·log|V|+|E|·log|V|)
    def dijkstra_mst(self, start):
        dist = {v: float('inf') for v in range(self.size)}
        parent = {v: None for v in range(self.size)}
        dist[start] = 0

        #min-heap priority queue (distance, vertex)
        min_heap = [(0, start)]

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)   #extract min

            for v, weight in self.adj_list[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    parent[v] = u
                    heapq.heappush(min_heap, (dist[v], v))

        return dist, parent
