class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in stones:
            heapq.heappush(h,-i)
        print(h)

        while len(h) > 1:
            top1 = -heapq.heappop(h)
            top2 = -heapq.heappop(h)

            if top1 > top2:
                top1 = top1 - top2
                heapq.heappush(h,-top1)
            elif top2 > top1:
                top2 = top2 - top1
                heapq.hepapush(h,top2)
        if len(h) == 0:
            return 0
        else:
            return -heapq.heappop(h)
        