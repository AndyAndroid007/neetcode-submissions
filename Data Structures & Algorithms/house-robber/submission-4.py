class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        def recurse(i):
            if i == 0:
                return nums[i]
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            pick = nums[i] + recurse(i-2)
            notpick = 0 + recurse(i-1)
            dp[i] = max(pick, notpick)
            return dp[i]
        return recurse(len(nums)-1)
        
        