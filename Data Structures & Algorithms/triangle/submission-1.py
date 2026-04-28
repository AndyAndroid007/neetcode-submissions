class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m-1])
        dp = [[-1]*n for _ in range(n)]
        # def recurse(i,j):
        #     if i == n-1:
        #         return triangle[n-1][j]
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     else:
        #         down = diag = float('inf')
        #         down = triangle[i][j] + recurse(i+1,j)
        #         diag = triangle[i][j] + recurse(i+1,j+1)
        #         dp[i][j] = min(down, diag)
        #         return dp[i][j]
        # return recurse(0,0)
        for j in range(n):
            dp[m-1][j] = triangle[m-1][j]
        
        for i in range(m-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]
    

        