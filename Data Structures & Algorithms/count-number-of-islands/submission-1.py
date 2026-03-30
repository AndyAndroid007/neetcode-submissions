class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def visit(x,y):
            visited.add((x,y))
            for dx,dy in directions:
                newx = x + dx
                newy = y + dy
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == "1" and (newx,newy) not in visited:
                    visit(newx,newy)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visit(i,j)
                    count+=1
        return count
        
        