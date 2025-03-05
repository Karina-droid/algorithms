#works for graphs with negative edges
#|V|*|E|
def bellmanFord(V, edges, src):
    dist = {v: float('inf') for v in range(V)}
    dist[src] = 0

    # Relaxation of all the edges V times, not (V - 1) as we
    # need one additional relaxation to detect negative cycle
    for i in range(V):
        for edge in edges:
            u, v, weight = edge
            if dist[u] == float('inf') and dist[u] + weight < dist[v]:
                #if there is a Vth relaxation, then there is a negative cycle
                return -1
            dist[v] = dist[u] + weight
    return dist