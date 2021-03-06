class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        subset = []
        results = []
        counter = Counter(nums)
        self.dfs(nums, subset, results, counter)
        return results
        
        
    def dfs(self, nums, subset, results, counter):
        if len(subset) == len(nums):
            results.append(subset[:])
            return
        
        for num in counter:
            if counter[num] > 0:
                
                subset.append(num)
                counter[num] -= 1
                self.dfs(nums, subset, results, counter)
                counter[num] += 1
                subset.pop()
        
        return