import numpy as np

DIAGONAL = 1
LEFT = 2
UP = 3

#O(m*n)
def LCS(X, Y):
    """fills the table C which stores the length of the longest common subsequence of two strings X and Y,
       B with the arrows to restore the solution """
    C = np.zeros((len(X), len(Y)), type=int)
    B = np.zeros((len(X), len(Y)), type=int)
    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                C[i][j] = C[i-1][j-1] + 1
                B[i][j] = DIAGONAL
            else:
                if C[i][j-1] >= C[i-1][j]:
                    C[i][j] = C[i][j-1]
                    C[i][j] = LEFT
                else:
                    C[i][j] = C[i-1][j]
                    C[i][j] = UP
    return (C,B)

#O(n+m)
def print_LCS(B, X, i, j):
    if i==0 or j==0: return
    if B[i][j] == DIAGONAL:
        print_LCS(B, X, i-1, j-1)
        print(X[i])
    elif B[i][j] == LEFT:
        print_LCS(B, X, i, j-1)
    else:
        print_LCS(B, X, i-1, j)
