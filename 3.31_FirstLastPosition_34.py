class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0:
            return [-1, -1]
        
        res = [-1, -1]  
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
                
        res[0] = start
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        res[1] = end
        
        print(res)
        if res[0] <= res[1]:
            return res
        else:
            return [-1, -1]