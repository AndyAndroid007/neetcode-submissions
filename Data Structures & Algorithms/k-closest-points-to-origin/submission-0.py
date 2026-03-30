class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        final = []
        for x,y in points:
            dist = (x**2 + y**2)**0.5
            heapq.heappush(h,(dist,x,y))
        for i in range(k):
            d,a,b = heapq.heappop(h)
            final.append([a,b])
        return final
        
        