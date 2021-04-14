class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return None
        
        mini, maxi = 1, 1
        res = -sys.maxsize
        for i in nums:
            a = mini * i
            b = maxi * i
            mini = min(a, b, i)
            maxi = max(a, b, i)
            res = max(res, maxi)
            
        return res
        