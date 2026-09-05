class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        def dfs(x,y,s):
            for dx,dy in directions:
                newx = x+dx
                newy = y+dy
                if 0 <= newx < m and 0 <= newy < n and heights[newx][newy] >= heights[x][y] and (newx,newy) not in s:
                    s.add((newx,newy))
                    dfs(newx,newy,s)
        
        pacific_reachable = set()
        atlantic_reachable = set()

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0) and (i,j) not in pacific_reachable:
                    pacific_reachable.add((i,j))
                    dfs(i,j,pacific_reachable)
                if (i == m-1 or j == n-1) and (i,j) not in atlantic_reachable:
                    atlantic_reachable.add((i,j))
                    dfs(i,j,atlantic_reachable)
        
        result = []
        
        for a,b in pacific_reachable:
            if (a,b) in atlantic_reachable:
                result.append([a,b])
        return result



        