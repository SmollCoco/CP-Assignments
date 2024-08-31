class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)

        stck = []
        for p, s in cars:
            timeToReachTarget = (target - p) / s
            if not stck or stck[-1] < timeToReachTarget:
                stck.append(timeToReachTarget)

        return len(stck)

