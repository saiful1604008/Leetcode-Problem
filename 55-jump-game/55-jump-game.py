class Solution:
    def canJump(self, nums: List[int]) -> bool:   
        if len(nums) < 2:
            return True
        
        dp = [0 for _ in range(len(nums)+1)]
        dp[0] = nums[0]
        
        for i in range(1,len(nums)):
            if dp[i-1] == 0:
                return False
        
            dp[i] = max(nums[i], dp[i-1]-1)
    
        return True
        

        