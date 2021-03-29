class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        if k <= 1:
            return 0
        
        left = 0
        result = 1
        count = 0
        
        for i in range(len(nums)):
            result = result * nums[i]
            while result >= k:
                result = result / nums[left]
                left += 1
            count += i - left + 1
        
        return count