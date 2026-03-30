class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        def backtrack(arr,s,start):
            rem = target - s
            if rem < 0:
                return
            
            if rem == 0:
                results.append(arr.copy())
                return
            
            if rem > 0:
                for i in range(start,len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    if candidates[i] > rem:
                        break
                    else:
                        arr.append(candidates[i])
                        backtrack(arr,s+candidates[i],i+1)
                        arr.pop()
        
        backtrack([],0,0)
        return results



        