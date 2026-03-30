class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            d = dict()
            for j in range(i+1,len(nums)):
                diff = target - nums[j]
                if diff in d:
                    triplet = tuple(sorted([nums[i],nums[j],nums[d[diff]]]))
                    output.add(triplet)
                else:
                    d[nums[j]] = j
        return list(map(list,output))


        