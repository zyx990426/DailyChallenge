class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle) == 0:
            return None
        
        
# Approach 1: DP, Change original triangle, top-down 
#         for i in range(1, len(triangle)):
#             for j in range(len(triangle[i])):
#                 if j == 0:
#                     triangle[i][j] += triangle[i - 1][j]
#                 elif j == len(triangle[i]) - 1:
#                     triangle[i][j] += triangle[i - 1][j - 1]
#                 else:
#                     triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
                    
#         return min(triangle[-1])
    
# Approach 2: DP, Do not change original triangle, bottom up, the first one in res in the minimum
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
                
        return res[0]