class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def dp(i):
            if i == 0:
                return cost[0]
            
            if i == 1:
                return cost[1]
            
            if i not in memo:
                memo[i] = min(dp(i-1), dp(i-2)) + cost[i]
            
            return memo[i]
        
        return min(dp(n-1), dp(n-2))