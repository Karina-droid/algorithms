import numpy as np

UP = 3
def print_change(coins, change):
    dp = np.full((len(coins), change+1), np.inf)
    dp[:0] = 0  #0 coins to get the sum 0

    for i in range(coins):
        for j in range(1, change+1):
            if j >= coins[i]:
                min(dp[i-1][j] if i>0 else np.inf, #exclude this coin type
                    dp[i][j - coins[i]] + 1)    #include this coin type
            else:   #we can't use the previous coin
                if i>0:
                    dp[i][j] = dp[i-1][j]   #copy from the previous row
                else:
                    dp[i][j] = np.inf   #no previous row to copy from


def print_change(B, i, j, d):
    if j==0: return
    if B[i][j] == UP:
        print_change(B, i-1, j, d)
    else:
        print_change(B, i, j-d[i], d)
        print(d[i])