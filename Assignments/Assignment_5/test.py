"""
m: Constraining weight
n: numbers of objects
"""

objects = [(1, 2), (2, 3), (5, 4), (6, 5)]
m = 8
n = 4

def knapsack():
    v = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        pi, wi = objects[i - 1]  # The '-1' is just for correct indexing
        for w in range(1, m + 1):
            v[i][w] = max(v[i - 1][w], v[i - 1][w - wi] + pi if w - wi >= 0 else -1)

    res = 0
    curr = m
    for i in range(n, 0, -1):
        if curr in v[i] and curr not in v[i - 1]:
            res += objects[i - 1][0]
            curr -= objects[i - 1][1]

    print(res)

knapsack()

