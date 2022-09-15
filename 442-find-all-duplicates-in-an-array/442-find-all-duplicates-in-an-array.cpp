class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
    vector <int> v;
    //int a[] = {1,2,1,4,4};
    int n;
    n = nums.size();
    map <int,int> mp;
    
    for(int i = 0; i < n; i++){
        mp[nums[i]]++;
        
        if (mp[nums[i]] > 1)
            v.push_back(nums[i]);
        
    }
    return v;
    }
};