class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        current = 0
        
        for i in range(0,len(nums)):
            current = current + nums[i]
            res.append(current)
            
        return res
            