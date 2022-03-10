class Solution:
    def arrangeCoins(self, n: int) -> int:
        k, i = 0, 1
        
        while n >= i:
            n = n - i
            k = k + 1
            i += 1
            
        return k 