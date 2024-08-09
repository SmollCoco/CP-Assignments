routes = range(1, int(input()) + 1)

for route in routes:
    numStops = int(input())
    ratings = [int(input()) for _ in range(numStops - 1)]

    res = 0
    curr = 0
    start, finish = 1, 1
    mStart, mFinish = 1, 1
    i = 2

    for rating in ratings:
        curr += rating
        mFinish += 1
        if curr > res:
            res = curr
            start = mStart
            finish = mFinish
        elif curr == res and mStart - mFinish < start - finish:
            start = mStart
            finish = mFinish
        if curr < 0:
            curr = 0
            mStart = i
        i += 1

    print(
        f"The nicest part of route {route} is between stops {start} and {finish}"
        if res > 0
        else f"Route {route} has no nice parts"
    )
