class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        mid = 0
        minNum = float('inf')
        while i < j:
            mid = (i + j)//2
            if nums[j] < nums[mid]:
                i = mid + 1
            else:
                j = mid
            
        return nums[i]


        