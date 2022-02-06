class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for x in nums:
            new_subset = [subset + [x] for subset in result]
            result.extend(new_subset)
        
        return result
            