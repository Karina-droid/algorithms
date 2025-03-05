from collections import deque

#O(|V|+|E|), with print_path - O(V^2)
def BFS(G, s):
    """
    Performs the Breadth-First-Search starting from s
    param G: graph represented as an adjacency list {node: neihbors
    param s: source vertex
    returns (π,d) -> parent dictionary and distance dictionary
    """
    d = {}  #distance dictionary
    pi = {} #parent dictionary
    C = {} #color dictionary
    bipartite = True

    #initialize all nodes
    for u in G:
        d[u] = float('inf')
        pi[u] = None
        C[u] = "White"

    #start BFS from source node s
    d[s] = 0
    pi[s] = None
    C[s] = "Grey"
    Q = deque([s])

    while Q:
        u = Q.popleft()
        for v in G[u]:  #iterate over all adjacent nodes
            if d[v] == d[u]:
                bipartite = False
            elif C[v] == "White":
                d[v] = d[u] + 1
                pi[v] = None
                Q.append(v)
        C[u] = "Black"
    return pi, d

#prints a path from s to u
def print_path(s, u, pi):
    if u==s: print(s)
    else:
        if pi[u]==None:
            print("no path from s to u")
        else:
            print_path(s, pi[u], pi)
            print(u)

#O(|V|+|E|)
def DFS(G):
    """ params G: represents the graph G as an adjacency list {node: neighbors}
        return: (pi, d, f) -> parent dictionary, discovery times, finishing times
    """
    global Time
    Time = 0
    d = {}  #discovery time
    f = {}  #finishing time
    pi = {} #parent dictionary
    C = {}  #color dictionary

    #Initialize all nodes
    for u in G:
        C[u] = None
        pi[u] = None
        d[u] = float('inf')
        f[u] = float('inf')

    #visit all nodes
    for u in G:
        if C[u] == "White":
            DFS_visit(G, u, C, d, f, pi)

    return pi, d, f

#running DFS is part: bipartite?, topoligical sorting, kosaraju's algo for scc
def DFS_visit(G, u, C, d, f, pi):
    Time += 1
    d[u] = Time
    C[u] = "Grey"   #mark node as visited
    #explore the neighbors
    for v in G[u]:
        if C[v] == "White": #if unvisited, explore recursively
            pi[v] = u
            DFS_visit(G, v, C, d, f, pi)
    C[u] = "Black"  #fully explored
    Time += 1
    f[u] = Time

