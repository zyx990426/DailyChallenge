class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0:
            return [-1, -1]
        
        result = [-1, -1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            result[0] = start
        elif nums[end] == target:
            result[0] = end
        
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        
        if nums[end] == target:
            result[1] = end
        elif nums[start] == target:
            result[1] = start
        
        return result