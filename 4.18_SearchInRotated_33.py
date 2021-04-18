class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        
        
        while start + 1 < end:
            mid = (start + end) // 2
            check = nums[end]
            if nums[mid] == target:
                return mid
            elif nums[mid] > check:
                if nums[mid] > target and nums[start] <= target: # mid的左边有序，判断target也在有序范围内的情况
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target and nums[end] >= target: # mid的右边有序，判断target也在有序范围内的情况
                    start = mid
                else:
                    end = mid
                
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1