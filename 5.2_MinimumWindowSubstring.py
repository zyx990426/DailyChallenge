class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = {}
        for q in t:
            if q in dicT:
                dicT[q] += 1
            else:
                dicT[q] = 1
                
        dics = {}
        count = 0
        start = 0
        result = ''
        for i in range(len(s)):
            if s[i] in dicT:
                if s[i] in dics:
                    dics[s[i]] += 1
                else:
                    dics[s[i]] = 1
                    
                if dicT[s[i]] == dics[s[i]]:
                    count += 1
            
            if count == len(dicT):
                while s[start] not in dicT or dicT[s[start]] < dics[s[start]]:
                    if s[start] in dicT and dicT[s[start]] < dics[s[start]]:
                        dics[s[start]] -= 1
                    start += 1
            
                if result == '' or len(result) > i - start + 1:
                    result = s[start: i + 1]
            
        return result
                    