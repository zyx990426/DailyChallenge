class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        nums.sort()
        longest = 1
        curr  = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:       
                curr += 1
                
            elif nums[i] == nums[i - 1]:
                continue
            else:
                longest = max(longest, curr)
                curr = 1
                
        return max(longest, curr)