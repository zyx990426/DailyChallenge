class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        if not arr or len(arr) == 0:
            return result
        
        start, end = 0, len(arr) - 1
        start, end = self.BinarySearch(start, end, arr, x)
        
        
        
        for _ in range(k):
            if start < 0:
                result.append(arr[end])
                end += 1
            elif end > len(arr) - 1:
                result.append(arr[start])
                start -= 1
            elif end <= len(arr) - 1 and start >= 0 and abs(arr[start] - x) > abs(arr[end] - x):
                result.append(arr[end])
                end += 1
            elif end <= len(arr) - 1 and start >= 0 and abs(arr[start] - x) <= abs(arr[end] - x):
                result.append(arr[start])
                start -= 1
        
        result.sort()
        
        return result
        
        
    def BinarySearch(self, start, end, arr, x):
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] > x:
                end = mid
            else:
                start = mid
                
        return start, end