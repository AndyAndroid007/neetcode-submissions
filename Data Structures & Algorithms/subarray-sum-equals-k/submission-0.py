class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = {0:1}
        runningSum = 0
        count = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum - k in p:
                count += p[runningSum-k]
            p[runningSum] = p.get(runningSum,0)+1
        return count

        