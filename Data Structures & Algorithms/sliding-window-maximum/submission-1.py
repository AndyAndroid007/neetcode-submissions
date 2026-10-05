class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        n = len(nums)
        final = []
        for j in range(n):
            heapq.heappush(h, (-nums[j],j))
            if j >= k-1:
                while h[0][1] < j-k+1:
                    heapq.heappop(h)
                final.append(-h[0][0])

                
        return final
                

        