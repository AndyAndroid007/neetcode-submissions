class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        for i in d.keys():
            if d[i] > 1:
                return True
        return False



         