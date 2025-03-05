import numpy as np

def extend_shortest_paths(D_prev, W, n):
    ''' D_prev is the previous shortest path matrix
        W is the weight matrix
        n is the number of vertices '''
    D_new = np.full((n,n), float('inf'))

    #updating shortest paths
    for i in range(n):
        for j in range(n):
            for k in range(n):
                D_new[i][j] = min(D_new[i][j], D_prev[i][k] + W[k][j])
    return D_new

#O(V^4)
def slow_all_pairs_shortest_paths(W):
    n = len(W)
    D = W.copy()

    for m in range(1, n-1):
        D = extend_shortest_paths(D, W, n)

    return D


#O(V^3 * logV)
def faster_all_pairs_shortest_paths(W):
    n = len(W)
    D = W.copy()
    m = 1       #the initial number of steps in path computation

    while m < n-1:
        D = extend_shortest_paths(D, D, n)
        m *= 2

    return D

#works for both directed and undirected weighted graphes, with both positive and negative edges
#doesn't work for graphs with negative cycles
#O(n^3)
def Floyd_Warshall(W):
    '''for each vertex k we check if a shorter path exists between i and j using k as intermidiate node'''
    n = len(W)
    dist = W.copy()

    for k in range(n):  #intermidiate vertex
        for i in range(n):  #start vertex
            for j in range(n):  #end vertex
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
