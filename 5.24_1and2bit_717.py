class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits or len(bits) == 0:
            return None
        
        i = 0
        n = len(bits) - 1
        while i < n:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        
        if i == n:
            return True
        return False