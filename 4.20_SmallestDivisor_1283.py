class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if not nums or len(nums) == 0:
            return None
        
        start = 1
        end = 1000000
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.check(nums, threshold, mid):
                end = mid
            else:
                start = mid
                
        if self.check(nums, threshold, start):
            return start
        return end
            
            
    def check(self, nums, threshold, div):
        summation = 0
        for i in nums:
            summation += math.ceil(i / div)
        
        if summation > threshold:
            return False
        return True