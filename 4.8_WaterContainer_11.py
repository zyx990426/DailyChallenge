class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0
        
        maxout = 0
        left, right = 0, len(height) - 1
        while left <= right:
            shorter = min(height[left], height[right])
            maxout = max(maxout, shorter * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxout