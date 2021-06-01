class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        r1, r2 = 0, 0
        for i in range(len(s)):
            r1 = self.validPalindrome(s, i, i, r1)
            r2 = self.validPalindrome(s, i, i + 1, r2)
            
        return r1 + r2
        
    
    def validPalindrome(self, s, left, right, result):
        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            else:
                break
                
        return result