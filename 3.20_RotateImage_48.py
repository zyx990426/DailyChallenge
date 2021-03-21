class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 0:
            return matrix
        
        self.transpose(matrix)
        self.reverse(matrix)
        
        return
    
    
    def transpose(self, matrix):
        n = len(matrix)
        
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return

    
    def reverse(self, matrix):
        n = len(matrix[0])
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
        return 