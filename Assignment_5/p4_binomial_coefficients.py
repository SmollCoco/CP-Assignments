t = int(input())

for _ in range(t):
    m = int(input())

    def eC(n: int, k: int) -> int:
        ret = 1
        for i in range(1, k + 1):
            if ret > m:
                return m + 1
            ret *= (n - i + 1) / i

        return round(ret)

    res = []
    k = 1
    while eC(k, k) <= m:
        k += 1
    while k:
        l, r = k, m + 1
        best = -1
        while l <= r:
            mid = round((l + r) / 2)
            if eC(mid, k) < m:
                l = mid + 1
            elif eC(mid, k) > m:
                r = mid - 1
            else:
                best = mid
                break

        if best != -1:
            if k < best - k:
                res.append((best, k))
                res.append((best, best - k))
            elif k == best - k:
                res.append((best, k))

        k -= 1

    print(l := len(res))
    for i in range(l - 1):
        n, k = res[i]
        print(f"({n},{k})", end=" ")
    n, k = res[l - 1]
    print(f"({n},{k})")
