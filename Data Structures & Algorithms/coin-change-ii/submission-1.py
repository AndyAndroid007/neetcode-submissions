class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]

        def func(ind, amt):
            if ind == n or amt < 0:
                return 0

            if amt == 0:
                return 1
            
            if dp[ind][amt] != -1:
                return dp[ind][amt]
            
            buy = 0
            if amt - coins[ind] >= 0:
                buy = func(ind,amt-coins[ind])
            notbuy = func(ind+1,amt)

            dp[ind][amt] = buy + notbuy
            return dp[ind][amt]
        
        return func(0,amount)
