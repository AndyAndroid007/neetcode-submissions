class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                ans = [d[diff],i]
                return ans
            else:
                d[nums[i]] = i
         
        