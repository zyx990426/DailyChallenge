class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        result = 0
        left, right = 0, len(height) - 1
        while left <= right:
            mini = min(height[left], height[right])
            if mini == height[left]:
                left += 1
                while left <= right and height[left] < mini:
                    result += mini - height[left]
                    left += 1
            else:
                right -= 1
                while left <= right and height[right] < mini:
                    result += mini - height[right]
                    right -= 1
        return result