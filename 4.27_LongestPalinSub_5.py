class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        
        maxlength = 0
        result = ''
        for i in range(len(s)):
            j, k = i, i
            
            while k < len(s) - 1 and s[k] == s[k + 1]: # 处理偶数情况
                k += 1
                
            sublength = k - j + 1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    sublength += 2
                    j -= 1
                    k += 1
                else:
                    break
            if sublength > maxlength:
                maxlength = sublength
                result = s[j + 1: k]
        
        return result