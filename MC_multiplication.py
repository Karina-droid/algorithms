#O(n^3)

import numpy as np

#fill the table to store calculated m(i,j)
def MC(P): #P is a vector of matrices' length
    n = len(P) - 1
    m = np.full((n+1, n+1), float('int'))   #min number of actions to multiply A_i * A_j
    s = np.zeros((n+1, n+1), type=int)  #the optimal position of k
    for i in range(n):
        m[i][i] = 0
    for l in range(n):   #i is the starting index of the current matrix chain
        for i in range(n-l+1):
            j = i + l -1
            m[i][j] = float('inf')
            for k in range(i,j-1):  #try all possible parenthesis positions, k is the split point
                #P[i-1] rows in the first matrix, P[k] common dimension (columns of first matrix, rows of second), P[j] - columns of second
                q = m[i][k] + m[k+1][j] + P[i-1]*P[k]*P[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k     #the placement of k that gives min m[i][j]
    return (m,s)