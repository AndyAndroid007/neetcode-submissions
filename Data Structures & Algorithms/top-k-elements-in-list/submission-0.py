class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        final = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for ele,cnt in count.items():
            final[cnt].append(ele)
        res = []
        for i in range(len(final)-1,0,-1):
            for a in final[i]:
                res.append(a)
                if len(res) == k:
                    return res
            



        