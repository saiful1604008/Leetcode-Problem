class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(20000)
        def dp(left,right,i):
            if i == len(multipliers):
                return 0
            
            a = nums[left]*multipliers[i] + dp(left+1, right, i+1)
            b = nums[right]*multipliers[i] + dp(left, right-1, i+1)
            return max(a,b)
        
        dp.cache_clear()
        return dp(0, len(nums)-1, 0)