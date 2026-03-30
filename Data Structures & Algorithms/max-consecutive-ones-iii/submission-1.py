class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount = 0
        maxL = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[i] == 0:
                    zeroCount-=1
                i+=1
            maxL = max(maxL, j-i+1)
        maxL = max(maxL,j-i+1)
        return maxL
            

        