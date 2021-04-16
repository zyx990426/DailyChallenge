class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return None
        
        start, end = 0, len(nums) - 1
        
        start, end = self.binarySearch(nums, start, end)
        
        if nums[start] <= nums[end]:
            return nums[start]
        return nums[end]
        
        
    def binarySearch(self, nums, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1
                
        return start, end