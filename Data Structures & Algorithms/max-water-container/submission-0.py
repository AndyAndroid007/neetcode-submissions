class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        area = 0
        while i <= j and j < len(heights):
            l = min(heights[i],heights[j])
            b = j-i
            area = max(area,l*b)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return area
        
        