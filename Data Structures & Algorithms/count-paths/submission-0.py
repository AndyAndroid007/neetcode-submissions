class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]

        def func(i,j):
            if i == m-1 and j == n-1:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            down = right = 0

            if i < m-1:
                down = func(i+1,j)
            if j < n-1:
                right = func(i,j+1)

            dp[i][j] = down + right
            return dp[i][j]
        
        return func(0,0)

        