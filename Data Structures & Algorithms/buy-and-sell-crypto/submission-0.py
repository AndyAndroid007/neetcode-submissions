class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minb = prices[0]
        maxdiff = 0
        for i in range(1,len(prices)):
            if prices[i] < minb:
                minb = prices[i]
            else:
                maxdiff = max(maxdiff,prices[i]-minb)
        return maxdiff        
        