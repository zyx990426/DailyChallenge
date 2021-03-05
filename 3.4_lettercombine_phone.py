class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        subset = []
        results = []
        if not digits or len(digits) == 0:
            return []
       
        
        self.dfs(digits, phone, subset, results,  0)
        return results
    
    
    def dfs(self, digits, phone, subset, results, index):
        
        if len(subset) == len(digits):
            results.append("".join(subset))
            return
        
        smalllist = phone[digits[index]]
        for i in smalllist:
            subset.append(i)
            
            self.dfs(digits, phone, subset, results, index+ 1)
            
            subset.pop()