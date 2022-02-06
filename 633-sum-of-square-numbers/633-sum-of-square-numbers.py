class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        num = int(sqrt(c))
        for a in range(num+1):
            b = sqrt(c-(a*a))
            if b == int(b):
                return True
            
        return False

        

            
        
        