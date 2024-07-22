# Link to YT video: https://youtu.be/JdApbYRLEWM

from queue import PriorityQueue

while True:
    n = int(input())
    if not n:
        break

    nums = list(map(int, input().split()))

    pQ = PriorityQueue()
    for num in nums:
        pQ.put(num)

    res = 0
    while pQ.qsize() > 1:
        cost = pQ.get() + pQ.get()
        res += cost
        pQ.put(cost)

    print(res)

