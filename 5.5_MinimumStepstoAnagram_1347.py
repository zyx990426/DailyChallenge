class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        dic = {}
        
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
                
        for j in range(len(t)):
            if t[j] in dic and dic[t[j]] > 0:
                dic[t[j]] -= 1
            else:
                count += 1
                
        return count