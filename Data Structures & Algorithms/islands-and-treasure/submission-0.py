class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            x,y = q.popleft()
            curr = grid[x][y]
            for dx,dy in directions:
                newx = x+dx
                newy = y+dy
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] != -1:
                    if curr + 1 < grid[newx][newy]:
                        grid[newx][newy] = curr+1
                        q.append((newx,newy))
        
        