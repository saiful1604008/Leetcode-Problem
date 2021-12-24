class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        #if n == 1:
            #return 
        t0, t1, t2 = 0, 1, 1
        for i in range(2,n):
            result = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = result
        
        return t2