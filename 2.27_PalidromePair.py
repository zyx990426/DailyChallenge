class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words or len(words) == 0:
            return []
        
        output = []
        worddict = {word: i for i, word in enumerate(words)}
        
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                prefix = words[i][:j]
                sufix = words[i][j:]
                
                if prefix == prefix[::-1]:
                    back = sufix[::-1]
                    if sufix[::-1] in worddict and back != words[i]:
                        output.append([worddict[sufix[::-1]], i])
                        
                if sufix == sufix[::-1]:
                    back = prefix[::-1]
                    if j != len(words[i]) and prefix[::-1] in worddict and back != words[i]:
                        output.append([i ,worddict[prefix[::-1]]])
                        
        return output
        
        
        

        
        
#         if not words or len(words) == 0:
#             return []
        
#         output = []
#         for i in range(len(words)):
#             for j in range(len(words)):
#                 if words[i] != words[j]:
#                     con = words[i] + words[j]
#                     if self.isPalindrome(con):
#                         output.append([i, j])
        
#         return output
    
    
#     def isPalindrome(self, word):
#         if not word or len(word) == 0:
#             return True
        
#         left, right = 0, len(word) - 1
#         while left <= right:
#             if word[left] != word[right]:
#                 return False
#             else:
#                 left += 1
#                 right -= 1
#         return True