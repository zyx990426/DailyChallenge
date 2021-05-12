class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        result = [0] * len(nums)
        start, end = 0, len(nums) - 1
        pointer = len(nums) - 1
        while start <= end and pointer >= 0:
            if (nums[start]**2) < (nums[end]**2):
                result[pointer] = nums[end]**2
                pointer -= 1
                end -= 1
            else:
                result[pointer] = nums[start]**2
                pointer -= 1
                start += 1
        
        return result