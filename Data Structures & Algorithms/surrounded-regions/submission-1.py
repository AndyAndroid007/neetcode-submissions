class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        m,n = len(board),len(board[0])
        visited = set()
        
        def dfs(x,y):
            visited.add((x,y))
            for dx,dy in directions:
                newx=x+dx
                newy=y+dy
                if 0 <= newx < m and 0 <= newy < n and (newx,newy) not in visited and board[newx][newy] == 'O':
                    board[newx][newy] = 'REACH'
                    dfs(newx,newy)
            
        
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'REACH'
                dfs(i,0)
            if board[i][n-1] == 'O':
                board[i][n-1] = 'REACH'
                dfs(i,n-1)
        
        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = 'REACH'
                dfs(0,j)
            
            if board[m-1][j] == 'O':
                board[m-1][j] = 'REACH'
                dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == 'REACH':
                    board[i][j] = 'O'


        