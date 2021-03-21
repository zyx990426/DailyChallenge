class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []
        subset = []
        results = []
        candidates.sort()
        return self.dfs(candidates, target, subset, results, 0)
        
        
        
    def dfs(self, candidates, target, subset, results, index):
        if target == 0:
            results.append(subset[:])
            
        for i in range(index, len(candidates)):
            if i > index and candidates[i - 1] == candidates[i]:
                continue
            if target < candidates[i]:
                break
            subset.append(candidates[i])
            self.dfs(candidates, target - candidates[i], subset, results, i + 1)
            subset.pop()
        
        return results