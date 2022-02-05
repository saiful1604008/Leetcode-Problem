class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        pallindrom_len = 0
        n = len(s)
        
        if n == 1: # case a
            return s
        
        for i in range(n):
            left,right = i, i    #case bab
            while left >= 0 and right < n and s[left] == s[right]:
                cur_lenght = right - left + 1
                if cur_lenght > pallindrom_len: 
                    result = s[left:right+1]
                    pallindrom_len = cur_lenght
                
                left -= 1
                right += 1 
                
        #return pallindrom_len
            
            left,right = i, i+1     #case bb
            while left >= 0 and right < n and s[left] == s[right]:
                cur_lenght = right - left + 1
                if cur_lenght > pallindrom_len:
                    result = s[left:right+1]
                    pallindrom_len = cur_lenght
                
                left -= 1
                right += 1
        
        return result
        
    