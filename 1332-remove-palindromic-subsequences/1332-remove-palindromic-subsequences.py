class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def ispalindrom(s):
            for i in range(0, int(len(s)/2)):
                if s[i] != s[len(s) - i - 1]:
                    return False
                
            return True
                
        if (ispalindrom(s)):
            return 1
        else:
            return 2
        
              
            