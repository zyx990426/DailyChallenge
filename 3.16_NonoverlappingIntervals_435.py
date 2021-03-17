class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[1])
        
        if len(intervals) == 1:
            return 0
        
        count = 0
        i = 0
        lastend = intervals[0][0]
        while i < len(intervals):
            if lastend > intervals[i][0]:
                i += 1
            else:
                lastend = intervals[i][1]
                i += 1
                count += 1
        
        return len(intervals) - count
            