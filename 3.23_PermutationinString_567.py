class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

#         Method1: Use Sorting
#         s1 = ''.join(sorted(s1))
#         k = len(s1)
        
#         for i in range(len(s2)):
#             s2_s = ''.join(sorted(s2[i:i + k]))
#             if s2_s == s1:
#                 return True
#         return False


#         Method2: Use Hashtable
        
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)
        for i in range(len(s2)):
            sub = s2[i:i + k]
            d2 = Counter(sub)
            if d1 == d2:
                return True
        return False
        