t = int(input())

for _ in range(t):
    n = int(input())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    g = int(input())
    strengths = [int(input()) for _ in range(g)]

    finalRes = 0
    for m in strengths:
        v = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            pi, wi = items[i - 1]  # The '-1' is just for correct indexing
            for w in range(1, m + 1):
                v[i][w] = max(v[i - 1][w], v[i - 1][w - wi] + pi if w - wi >= 0 else -1)

        finalRes += v[-1][-1]

    print(finalRes)

