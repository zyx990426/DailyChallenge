class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s or len(s) == 0:
            return []
        
        result = []
        right_most = {c:i for i, c in enumerate(s)}
        
        left, right = 0, 0
        for index, letter in enumerate(s):
            right = max(right, right_most[letter])
            
            if index == right:
                result += [right - left + 1]
                left = index + 1
                
        return result
        