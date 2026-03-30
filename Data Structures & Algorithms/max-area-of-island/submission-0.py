class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def traverse(i,j):
            grid[i][j] = 0
            size = 1
            for dx,dy in directions:
                newx = i + dx
                newy = j + dy
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 1:
                    size += traverse(newx,newy)
            return size
        m = len(grid)
        n = len(grid[0])
        maxSize = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxSize = max(maxSize, traverse(i,j))
        return maxSize
        
        