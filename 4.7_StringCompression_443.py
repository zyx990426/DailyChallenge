class Solution(object):
    def compress(self, chars):
        if not chars or len(chars) == 0:
            return 0
        
        left, i = 0, 0
        while i < len(chars):
            char = chars[i]
            length = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                length += 1
                i += 1
            chars[left] = char
            
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            
            left += 1
            i += 1
        
        return left