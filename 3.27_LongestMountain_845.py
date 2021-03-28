# Time Complexity: O(n)
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        
        i = 0
        maxlength = 0
        while i < len(arr) - 1:
            while i < len(arr) - 1 and arr[i] >= arr[i + 1]:
                i += 1
            peak = i
            while peak < len(arr) - 1 and arr[peak] < arr[peak + 1]:
                peak += 1
            bottom = peak
            while bottom < len(arr) - 1 and arr[bottom] > arr[bottom + 1]:
                bottom += 1
            if i < peak and peak < bottom:
                maxlength = max(maxlength, bottom - i + 1)
            i = bottom
        return maxlength
    
    
#Another Approach: For loop peak, and go to left and right (O(n^2))