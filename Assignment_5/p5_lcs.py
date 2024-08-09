while True:
    try:
        A = input()
        B = input()
        m, n = len(A), len(B)

        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if not i or not j:
                    memo[i][j] = 0
                    continue
                if A[i - 1] == B[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

        print(memo[m][n])
    except:
        break
