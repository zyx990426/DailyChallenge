class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return []
        
        intervals.sort(key = lambda x: x[0])
        
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            # elif intervals[i][0] <= result[-1][1] and intervals[i][1] > result[-1][1]:
            #     result[-1][1] = intervals[i][1]
            # else:
            #     continue
        return result