class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(arr,s,ind):
            if s == target:
                final.append(arr[:])
                return
            
            for i in range(ind, len(nums)):
                if nums[i] + s <= target:
                    arr.append(nums[i])
                    backtrack(arr, s + nums[i], i)
                    arr.pop()
        final = []
        backtrack([],0,0)
        return final