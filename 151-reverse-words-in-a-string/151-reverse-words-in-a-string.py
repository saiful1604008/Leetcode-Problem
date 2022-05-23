class Solution:
    def reverseWords(self, s: str) -> str:
        stack = s.split(' ')
        res = []
        while stack:
            current = stack.pop()
            if current != '':
                res.append(current)
            
        return " ".join(res)
        
            
            
            
            