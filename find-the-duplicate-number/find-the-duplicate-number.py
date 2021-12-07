class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 1, len(nums)-1

        while l < r:
            m = l + (r - l)//2
            c = 0
            
            for i in nums:
                if i <= m:
                    c+=1
        
            if c <= m:
                l = m + 1
            else:
                r = m
                
        return l