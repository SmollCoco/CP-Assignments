m = int(input())

for _ in range(m):
    n, k = map(int, input().split())

    adjList = [[] for i in range(n + 1)]
    for _ in range(k):
        u, v = map(int, input().split())
        adjList[u].append(v)
        adjList[v].append(u)

    def valid(v, blacks):  #Check whether a certain vertex can be colored
        for u in adjList[v]:
            if u in blacks:
                return False
        return True

    res_x, res_y = [0], [[]]
    n = [n]

    def backtrack(v=1, blacks=set(), b=0):
        if v > n[0]:
            if b > res_x[0]:
                res_y[0] = blacks.copy()
                res_x[0] = b
            return
        
        # Choose to color the current vertex black if possible
        if valid(v, blacks):
            blacks.add(v)
            backtrack(v + 1, blacks, b + 1)
            blacks.remove(v)
        
        # Choose to color the current vertex white
        backtrack(v + 1, blacks, b)

    backtrack()
    print(res_x[0])
    print(*res_y[0])
