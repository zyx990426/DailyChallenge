class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        subset = []
        self.dfs(n,k,1,subset, results)
        return results

    def dfs(self, n, k, index, subset, results):
        if len(subset) == k:
            results.append(list(subset))
            return 
        if index == n+1 or len(subset) > k:
            return
        for i in range(index, n+1):
            subset.append(i)
            self.dfs(n,k,i+1, subset,results)
            subset.pop()