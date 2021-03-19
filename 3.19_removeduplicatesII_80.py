class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        slow = 1
        count = 1
        index = 1
        
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                count += 1
                if count > 2:
                    index += 1
                    continue
            else:
                count = 1
            
            nums[slow] = nums[index]
            index += 1
            slow += 1
        return slow