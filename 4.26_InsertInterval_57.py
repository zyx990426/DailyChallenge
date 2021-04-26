class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        intervals.sort(key = lambda x: x[0])
        left = []
        merge = []
        right = []
        
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                left.append(intervals[i])
                i += 1
            elif intervals[i][0] > newInterval[1]:
                right.append(intervals[i])
                i += 1
            
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                i += 1