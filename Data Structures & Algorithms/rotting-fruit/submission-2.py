class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        m,n = len(grid),len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        count = 0
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                x,y = q.popleft()
                for dx,dy in directions:
                    newx=x+dx
                    newy=y+dy
                    if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 1:
                        fresh-=1
                        grid[newx][newy] = 2
                        q.append((newx,newy))
            count += 1
        
        if fresh > 0:
            return -1
        return count
        
                    

        