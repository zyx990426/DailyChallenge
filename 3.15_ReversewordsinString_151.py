class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        
#         words = s.split()[::-1]
        
#         return ' '.join(words)

        ans = ''
        p1, p2 = len(s) - 1, len(s) - 1
        while p1 >= 0 and p2 >= 0:
            while p1 >=0 and s[p1] == ' ':
                p1 -= 1
            p2 = p1
            print(p2)
            
            while p1 >= 0 and s[p1] != ' ':
                p1 -= 1
            ans += s[p1 + 1: p2 + 1] + ' '
            p2 = p1
            print(p2)
            
            while p1 >= 0 and s[p1] == ' ':
                p1 -= 1
                
        return ans[:-1]
        