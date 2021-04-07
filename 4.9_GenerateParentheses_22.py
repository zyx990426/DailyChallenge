class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        results = []
        subset = ''
        self.dfs(n, n, results, subset)
        return results
        
        
    def dfs(self, left, right, results, subset):
        if left < 0 or right < 0 or left > right:
            return 
        if left == 0 and right == 0:
            results.append(subset)
            return
        self.dfs(left - 1, right, results, subset + '(')
        self.dfs(left, right - 1, results, subset + ')')