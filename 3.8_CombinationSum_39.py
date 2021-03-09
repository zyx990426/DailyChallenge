lass Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []
        self.dfs(candidates, results, subset, target)
        return results
        
    
    def dfs(self, candidates, results, subset, target):
     
        if target < 0:
            return
        
        if target == 0:
            results.append(subset[:])
            return
        
        for i in range(len(candidates)):
            subset.append(candidates[i])
            self.dfs(candidates[i:], results, subset , target - candidates[i])
     
            subset.pop()
        
        return