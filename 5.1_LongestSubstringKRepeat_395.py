class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        
        result = 0
        for m in range(1, 27):
            result = max(result, self.helper(s, m ,k))
            
        return result
    
    def helper(self, s, m, k):
        result = 0
        dic = {}
        j = 0
        count = 0
        for i in range(len(s)):
            while j < len(s) and len(dic) <= m:
                if s[j] in dic:
                    dic[s[j]] += 1
                else:
                    dic[s[j]] = 1
                
                if dic[s[j]] == k:
                    count += 1
                
                if len(dic) == m and count == m:
                    result = max(result, j - i + 1)
                    
                j += 1
            
            dic[s[i]] -= 1
            if dic[s[i]] == k - 1:
                count -= 1
            if dic[s[i]] == 0:
                dic.pop(s[i], None)
        
        return result