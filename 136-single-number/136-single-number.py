class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = Counter(nums)
        #print(num)
        
        for i in nums:
            if num[i] == 1:
                return i
        