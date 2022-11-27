def binomialCoeff_recursive(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return binomialCoeff_recursive(n - 1, k - 1) + binomialCoeff_recursive(n - 1, k)

import math

#bottom-up
def binomialCoeff_DP2D(n, k):
    c = [[0 for x in range(k + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
    return c[n][k]

#1D array
def binomialCoeff_DP1D(n, k):
    c = [0 for x in range(k + 1)]
    c[0] = 1
    
    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            c[j] = c[j] + c[j - 1]
            j -= 1
    return c[k]
