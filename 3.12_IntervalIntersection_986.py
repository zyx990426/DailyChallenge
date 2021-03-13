class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        
        output = []
        p1, p2 = 0, 0
        
        while p1 < len(firstList) and p2 < len(secondList):
            low = max(firstList[p1][0], secondList[p2][0])
            high = min(firstList[p1][1], secondList[p2][1])
            
            if low <= high:
                output.append([low, high])
            
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
                
        return output