def trap(height: List[int]) -> int:
    n = len(height)
    i, j = 0, n - 1
    leftMax, rightMax = height[i], height[j]

    res = 0

    while i < j:
        if leftMax < rightMax:
            res += leftMax - height[i]
            i += 1
            if height[i] > leftMax:
                leftMax = height[i]
        else:
            res += rightMax - height[j]
            j -= 1
            if height[j] > rightMax:
                rightMax = height[j]

    return res

