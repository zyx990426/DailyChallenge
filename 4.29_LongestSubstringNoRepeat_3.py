class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        hashset = set()
        result = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                result = max(result, len(hashset))
                right += 1
            
            else:
                hashset.remove(s[left])
                left += 1
                
        return result