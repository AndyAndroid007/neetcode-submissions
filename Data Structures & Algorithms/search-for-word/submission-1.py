class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def backtrack(ind,i,j):
            if ind == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[ind]:
                return False
            
            temp = board[i][j]
            board[i][j] = '/'
            for di,dj in directions:
                new_i = i+di
                new_j = j+dj

                if backtrack(ind+1,new_i,new_j):
                    return True
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(0,i,j):
                        return True
        
        return False

        