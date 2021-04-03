class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums = sorted(nums)
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twosum(-nums[i], i + 1, len(nums) - 1, nums, results)
        return results
    
    def twosum(self, target, start, end, nums, results):
        if start >= end:
            return
        last_pair = None
        while start < end:
            if nums[start] + nums[end] == target:
                if (nums[start], nums[end]) != last_pair:
                    results.append([-target, nums[start], nums[end]])
                last_pair = (nums[start], nums[end])
                start += 1
                end -= 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
        return