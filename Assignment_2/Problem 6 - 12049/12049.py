# Link to YT video: https://youtu.be/NkVm-NIbJ3s

from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    l1 = input().split()
    l2 = input().split()

    mp = defaultdict(int)

    for num in l1:
        if num in l2:
            mp[num] += 1
            l2.remove(num)

    print(mp)

    res = m + n - 2 * sum(mp.values())
    print(res)

