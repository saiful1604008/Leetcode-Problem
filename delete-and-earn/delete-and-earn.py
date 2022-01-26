class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # frequency count of the array
        count = dict()
        for i in nums:
            if i in count:
                count[i] = count[i] + 1
            else:
                count[i] = 1
                
        # removing repeating val from the array       
        temp_list = []
        for i in nums:
            if i not in temp_list:
                temp_list.append(i)
        nums = temp_list
        nums = sorted(nums)

        earn1 = nums[0]*count[nums[0]]
        
        if nums[1] - nums[0] == 1:
            earn2 = max(earn1,nums[1]*count[nums[1]])
        else:
            earn2 = earn1 + nums[1]*count[nums[1]]
            
        dp = [0]*len(nums)
        dp[0] = earn1
        dp[1] = earn2
        
        for i in range(2,len(dp)):
            if nums[i] - nums[i-1] == 1:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i]*count[nums[i]])
            else:
                dp[i] = dp[i-1] + nums[i]*count[nums[i]]
        
        return dp[-1]