class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        cSet = set()

        def canPlace(x,y):
            if y in cSet:
                return False

            def diagCheck(x,y,dx,dy):
                while 0 <= x < n and 0 <= y < n:
                    if board[x][y] == 'Q':
                        return False
                    x += dx
                    y += dy
                return True
            
            diags = [[1,1],[-1,-1],[-1,1],[1,-1]]
            for dx,dy in diags:
                if not diagCheck(x,y,dx,dy):
                    return False

            return True
        
        final = []
        
        def backtrack(i):
            if i == n:
                ans = ["".join(r) for r in board]
                final.append(ans)
                return
        
            for j in range(n):
                if canPlace(i,j):
                    
                    board[i][j] = 'Q'
                    cSet.add(j)

                    backtrack(i+1)

                    board[i][j] = '.'
                    cSet.remove(j)
        
        backtrack(0)
        return final
            
                    
            

            
            

        
        