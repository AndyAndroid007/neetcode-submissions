class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)

        for i in range(1,len(height)):
            maxLeft[i] = max(maxLeft[i-1],height[i-1])
        
        for i in range(len(height)-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],height[i+1])

        for i in range(len(height)):
            a = min(maxLeft[i],maxRight[i]) - height[i]
            if a < 0:
                s+=0
            else:
                s+=a
        return s


        