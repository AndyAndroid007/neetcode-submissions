class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        left[0] = nums[0]
        right[-1] = nums[-1]
        
        for i in range(1,len(nums)):
            left[i] = nums[i]*left[i-1]
        for i in range(len(nums)-2,0,-1):
            right[i] = right[i+1]*nums[i]
        final = [1]*len(nums)
        print(left,right)
        final[0] = right[1]
        final[-1] = left[len(nums)-2]
        for i in range(1,len(nums)-1):
            final[i] = left[i-1]*right[i+1]
        return final


        