class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        subset = []
        results = []
        nums.sort()
        self.dfs(nums, subset, results, 0)
        return results
        
        
    def dfs(self, nums, subset, results, startindex):
        results.append(subset[:])
        
        for i in range(startindex, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i != startindex:
                continue
            subset.append(nums[i])
            self.dfs(nums, subset, results, i + 1)
            subset.pop()
        return