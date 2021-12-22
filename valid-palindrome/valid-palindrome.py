class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        second = len(s) - 1
        
        while(first <= second):
            if(not s[first].isalnum()):
                first += 1
                continue
                
            if(not s[second].isalnum()):
                second -= 1 
                continue
                
            if(s[first].lower() == s[second].lower()):
                first += 1
                second -= 1
                continue
            else:
                return False
        
        return True
    
                
            
            
            