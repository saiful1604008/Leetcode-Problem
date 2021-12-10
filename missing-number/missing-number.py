class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            result += nums[i]  
        
        return (n*(n+1)//2) - result