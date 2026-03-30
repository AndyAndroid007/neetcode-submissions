class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed):
            totalhours = 0
            for i in piles:
                totalhours += math.ceil(i/speed)
            return totalhours <= h
        left = 1
        right = max(piles)
        ans = float('inf')
        while left <= right:
            mid = (left+right)//2
            if check(mid):
                ans = min(ans,mid)
                right = mid-1
            else:
                left = mid+1
        return ans

        