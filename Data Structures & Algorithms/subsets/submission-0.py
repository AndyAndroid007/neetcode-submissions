class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(arr,start):
            results.append(arr.copy())
            for i in range(start,len(nums)):
                arr.append(nums[i])
                backtrack(arr,i+1)
                arr.pop()
        
        backtrack([],0)
        return results





        

        