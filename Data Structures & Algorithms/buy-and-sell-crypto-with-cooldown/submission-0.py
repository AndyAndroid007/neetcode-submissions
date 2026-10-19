class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]

        def func(ind, canBuy):
            if ind >= n:
                return 0
            print(ind,canBuy)
            if dp[ind][canBuy] != -1:
                return dp[ind][canBuy]
            
            x = 0
            if canBuy == 0:
                x = -prices[ind] + func(ind+1, 1)
                y = func(ind+1,canBuy)
            
            else:
                x = prices[ind] + func(ind+2, 0)
                y = func(ind+1, canBuy)

            
            dp[ind][canBuy] = max(x,y)
            return dp[ind][canBuy]
        
        return func(0,0)
        