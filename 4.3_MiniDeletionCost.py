class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        pre = 0 #pre is index of previous same letter with max cost
        
        for i in range(1, len(s)):
            if s[pre] != s[i]: pre = i
            else:
                res += min(cost[pre], cost[i])
                if cost[pre] < cost[i]: pre = i
                    
        return res