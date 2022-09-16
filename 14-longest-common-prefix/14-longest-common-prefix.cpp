class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans;
        int n = strs[0].length();
        for(int i = 0; i < n; i++){
            char ch = strs[0][i];
            int j;
            for(j = 1; j < strs.size(); j++){
                if (strs[j][i] != ch)
                    break;
            }
        if (j == strs.size()){
            ans += strs[0][i];
        }
        else{
            //cout << ans;
            return ans;
        }
    }
        
    return ans;
    }
};