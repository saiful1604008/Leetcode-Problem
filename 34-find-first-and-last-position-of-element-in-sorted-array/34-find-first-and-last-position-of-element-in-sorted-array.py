class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                
                if nums[mid] > target:
                    right = mid - 1
                
                if nums[mid] < target:
                    left = mid + 1
                
            if left >= len(nums) or nums[left] != target:
                return - 1
            
            #print(left)
            
            return left
        
        def right_bound(nums: List[int], target:int) -> int:
            left , right = 0, len(nums) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                
                if nums[mid] > target:
                    right = mid - 1
                
                if nums[mid] == target:
                    left = mid + 1
                    
            if right < 0 or nums[right] != target:
                return -1
            
            #print(right)
            
            return right
    
        
        return [left_bound(nums,target), right_bound(nums,target)]
        
    
        
    
                    