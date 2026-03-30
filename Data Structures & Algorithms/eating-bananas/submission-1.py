class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def satisfy(speed,total):
            count = 0
            for i in piles:
                count += math.ceil(i/speed)
            if count <= total:
                return True
            return False

        i = 1
        j = max(piles)
        minTime = float('inf')
        while i <= j :
            mid = (i + j)//2
            if satisfy(mid,h):
                minTime = min(minTime,mid)
                j = mid-1
            else:
                i = mid + 1
        return minTime


        