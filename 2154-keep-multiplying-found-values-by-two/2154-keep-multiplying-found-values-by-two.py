class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for __ in range(len(nums)):
            if original in list(nums):
                original *= 2
            else:
                break
        return original