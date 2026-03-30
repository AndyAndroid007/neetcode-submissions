class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()

        def backtrack(arr,start):
            final.append(arr.copy())

            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                backtrack(arr,i+1)
                arr.pop()
        backtrack([],0)
        return final

        