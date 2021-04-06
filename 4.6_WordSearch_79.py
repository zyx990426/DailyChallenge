class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board or len(board) == 0:
            return False
        
        m, n, k = len(board), len(board[0]), len(word)
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word):
                    return True
        return False
    
    
    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        temp = board[i][j]
        board[i][j] = '#'
        
        res = True
      
          
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = temp
        
        return res