class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        def traverse(i,j):
            visited[i][j] = True
            for dx,dy in directions:
                newx = i + dx
                newy = j + dy
                if 0 <= newx < m and 0 <= newy < n and not visited[newx][newy] and grid[newx][newy] == '1':
                    traverse(newx,newy)
            return
        count = 0
        for a in range(m):
            for b in range(n):
                if not visited[a][b] and grid[a][b] == '1':
                    traverse(a,b)
                    count+=1
        return count


        