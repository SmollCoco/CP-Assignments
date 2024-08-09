t = int(input())

for _ in range(t):
    m = int(input())

    memo = [[-1] * (n + 1) for n in range(m + 1)]
    for p in range(m + 1):
        memo[p][0] = 1
        memo[p][-1] = 1

    def comb(n, k):
        if k == n or k == 0:
            return memo[n][k]
        if memo[n][k] == -1:
            memo[n][k] = comb(n - 1, k - 1) + comb(n - 1, k)
        return memo[n][k]

    l = 0
    res = []

    for n in range(2, m + 1):
        for k in range(1, n // 2 + 1):
            if comb(n, k) == m:
                l += 2
                res.append((n, k))
                res.append((n, n - k))

    res.sort()

    print(l)
    print(*res)
