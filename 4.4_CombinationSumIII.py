class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        subset = []
        results = []
        self.dfs(nums, subset, results, 0, k, n)
        return results
    
    
    def dfs(self, nums, subset, results, index, k, target):
        if len(subset) == k and target == 0:
            results.append(subset[:])
            
        if target < 0:
            return
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, subset, results, i + 1, k, target - nums[i])
            subset.pop()