class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return None
        
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j <= n - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
                
        return False