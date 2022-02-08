class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        res2 = sorted_nums[-1] * sorted_nums[-2]
        res1 = sorted_nums[0] * sorted_nums[1]
        
        return res2 - res1 
    
            