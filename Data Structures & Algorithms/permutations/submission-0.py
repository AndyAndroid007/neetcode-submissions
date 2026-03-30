class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []

        def backtrack(arr,seen):
            if len(arr) == len(nums):
                final.append(arr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    arr.append(nums[i])
                    seen.add(nums[i])
                    backtrack(arr,seen)
                    seen.remove(nums[i])
                    arr.pop()
        backtrack([],set())
        return final
        