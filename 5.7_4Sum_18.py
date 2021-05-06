class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        result = []
        nums.sort()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sub_target = target - nums[i] - nums[j]
                self.twoSum(nums, j + 1, len(nums) - 1, sub_target, nums[i], nums[j], result)
        return result
                
                
                
                
                
    def twoSum(self, nums, start, end, target, p1, p2, result):
        if start >= end:
            return
        
        last_pair = None
        
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                if (nums[start], nums[end]) != last_pair and [p1, p2, nums[start], nums[end]] not in result:
                    result.append([p1, p2, nums[start], nums[end]])
                last_pair = nums[start], nums[end]
                start += 1
                end -= 1
        return