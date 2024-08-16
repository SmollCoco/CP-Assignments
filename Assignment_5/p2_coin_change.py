# Link to YouTube video: https://youtu.be/YU00ygEdoBY

while True:
    try:
        x = int(input())

        memo = [[0] + [1] * 5] + [[0] + [-1] * 5 for _ in range(x)]

        def numOfChange(x: int, n=5, available=[1, 5, 10, 25, 50]) -> int:
            if x - available[-1] >= 0 and memo[x - available[-1]][n] == -1:
                memo[x - available[-1]][n] = numOfChange(
                    x - available[-1], n, available
                )
            if memo[x][n - 1] == -1:
                memo[x][n - 1] = numOfChange(x, n - 1, available[:-1])

            a = memo[x - available[-1]][n] if x - available[-1] >= 0 else 0
            b = memo[x][n - 1] if x >= 0 else 0
            if x >= 0:
                memo[x][n] = a + b
            return a + b

        print(numOfChange(x))
    except:
        break
