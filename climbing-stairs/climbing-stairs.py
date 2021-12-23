class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        
        a, b = 1, 1
        for i in range(2,n+1):
            result = a + b
            b = a
            a = result
            
        return result    
            