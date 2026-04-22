class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev = nums[0]
        curr = 0
        for i in range(1, len(nums)):
            pick = nums[i]
            if i > 1:
                pick += prev2
            notpick = 0 + prev

            curr = max(pick, notpick)
            prev2 = prev
            prev = curr
        return prev
        
        