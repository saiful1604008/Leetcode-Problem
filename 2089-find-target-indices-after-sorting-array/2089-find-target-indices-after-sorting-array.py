class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        number = sorted(nums)
        
        for i in range(len(number)):
            if number[i] == target:
                res.append(i)
        
        return res