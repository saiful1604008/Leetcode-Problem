class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        if " " not in s:
            return len(s)
        
        for i in range(len(s)-1, -1, -1):
            if s[i]!= " ":
                counter += 1
                
            if counter >= 1 and s[i] == " ":
                return counter
            
        return counter
            