class Solution:
    def jump(self, nums: List[int]) -> int:
        count, left, right = 0, 0, 0
        while len(nums) - 1 > right:
            max_jump = 0
            for i in range(left,right+1):
                max_jump = max(max_jump, i+nums[i])
            left = right + 1
            right = max_jump
            count += 1
        
        return count
                
            
         
                
                
            
        
             
              