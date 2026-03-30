class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        d = Counter(nums)
        maxcount = 1
        for i in nums:
            count = 1
            a = i+1
            while a in d:
                count+=1
                a+=1
            maxcount = max(maxcount,count)
        return maxcount
            