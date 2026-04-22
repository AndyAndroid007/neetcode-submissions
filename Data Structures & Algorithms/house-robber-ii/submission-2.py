class Solution:
    def rob(self, nums: List[int]) -> int:
        def dpFunc(arr):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]
            
            dp = [0]*n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            for i in range(2, n):
                dp[i] = max(arr[i] + dp[i-2], dp[i-1])
            
            return dp[n-1]
        
        if len(nums) == 1:
            return nums[0]
        
        return max(dpFunc(nums[:-1]), dpFunc(nums[1:]))