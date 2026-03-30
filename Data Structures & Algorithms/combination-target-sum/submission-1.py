class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        def backtrack(arr,s,start):
            rem = target - s
            if rem < 0:
                return
            if rem == 0:
                results.append(arr.copy())
                return
            
            if rem > 0:
                for i in range(start,len(nums)):
                    if nums[i] > rem:
                        break
                    if nums[i] <= rem:
                        arr.append(nums[i])
                        backtrack(arr,s+nums[i],i)
                        arr.pop()
        backtrack([],0,0)
        return results
            

        