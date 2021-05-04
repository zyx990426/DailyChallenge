class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #左扫一遍， 右扫一遍
        
        if not nums or len(nums) == 0:
            return []
        
        result = [0] * len(nums)
        result[0] = 1
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        
        right = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] = right * result[j]
            right = right * nums[j]
            
        return result