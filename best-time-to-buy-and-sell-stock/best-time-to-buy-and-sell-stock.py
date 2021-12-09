class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        min1 = prices[0]
        profit = 0
        for i in prices[1:]:
            if i < min1:
                min1 = i
            else:
                t = i - min1
                if t > profit:
                    profit = t
                    
        return profit