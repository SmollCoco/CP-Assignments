n = int(input())

for _ in range(n):
    m, c = map(int, input().split())
    garments = [tuple(map(int, input().split())) for _ in range(c)]

    memo = [[None] * (c + 1) for _ in range(m + 1)]
    inf = float("inf")

    def search(money=m, g=0):
        if money < 0:
            return -inf
        if g == c:
            if memo[money][g] is None:
                memo[money][g] = m - money
            return memo[money][g]
        if memo[money][g] is None:
            memo[money][g] = max(
                search(money - garments[g][p], g + 1)
                for p in range(1, garments[g][0] + 1)
            )
        return memo[money][g]

    res = search()
    if res < 0:
        res = "no solution"

    print(res)
