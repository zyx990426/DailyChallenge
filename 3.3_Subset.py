class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        results = []
        self.dfs(nums, subset, results, 0)
        return results
        
        
    def dfs(self, nums, subset, results, startindex):
        
        results.append(subset[:])
        
        for i in range(startindex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, subset, results, i + 1)
            subset.pop()
        
        return