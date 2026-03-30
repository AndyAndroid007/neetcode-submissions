class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(arr,s,ind):
            if s == target:
                final.append(arr[:])
                return
            
            for i in range(ind, len(candidates)):
                if s + candidates[i] <= target:
                    if i > ind and candidates[i] == candidates[i-1]:
                        continue
                    arr.append(candidates[i])
                    backtrack(arr, s+ candidates[i], i+1)
                    arr.pop()
        final = []
        backtrack([],0,0)
        return final
        