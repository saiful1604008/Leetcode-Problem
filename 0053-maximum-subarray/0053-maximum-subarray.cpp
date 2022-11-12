class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int MaxSum = nums[0];
        int CurrSum = 0;
        
        for(int i=0; i < nums.size();i++){
            CurrSum += nums[i];
            if(CurrSum > MaxSum)
                MaxSum = CurrSum;
            
            if(CurrSum < 0) CurrSum = 0;
        }
        
        return MaxSum;
    }
};