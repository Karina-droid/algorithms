from collections import deque

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
            if C[v] == "White":
                d[v] = d[u] + 1
                pi[v] = None
                Q.append(v)
        C[u] = "Black"
    return pi, d

def DFS():
    pass

#prints a path from s to u
def print_path(s, u, pi):
    if u==s: print(s)
    else:
        if pi[u]==None:
            print("no path from s to u")
        else:
            print_path(s, pi[u], pi)
            print(u)