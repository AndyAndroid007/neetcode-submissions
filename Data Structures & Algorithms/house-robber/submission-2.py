class Solution:
    def rob(self, nums: List[int]) -> int:

        if 1 <= len(nums) <= 2:
            return max(nums)
        dp = [0]*(len(nums)+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            
            pick = nums[i] + dp[i-2]
            nonpick = 0 + dp[i-1]
            dp[i] = max(pick,nonpick)
        
        return dp[len(nums)-1]