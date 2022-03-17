class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score, val = 0, 1
        for i in range(len(s) - 1):
            if s[i: i+2] == '((':
                val *= 2
            
            if s[i: i+2] == '()':
                score += val
            
            if s[i: i+2] == '))':
                val //= 2
        
        return score
                
    