class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1
        target = nums[-1]
        start, end = self.BinerySearch(nums, start, end, target)
   
        if nums[start] <= nums[end]:
            return nums[start]
        return nums[end]
    
        
    def BinerySearch(self, nums, start, end, target):
  
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                start = mid
            else:
                end = mid
        return start, end