class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        main = {}
        for char in sentence:
            main[char] = True
        
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char not in main:
                return False
        
        return True
                
                
            
        