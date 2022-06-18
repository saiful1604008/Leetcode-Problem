class Solution {
public:
    string reverseWords(string s) {
        stack <char> st;
        string ans = "";
        int i;
        
        for (int i = 0; i < s.size(); i++){
            if (s[i] == ' '){
                while (!st.empty()){
                    ans.push_back(st.top());
                    st.pop();
                }
                
                ans.push_back(' ');
                
                
            }
            
            else if (i == s.size() - 1){
                st.push(s[i]);
                while (!st.empty()){
                    ans.push_back(st.top());
                    st.pop();
                }
            }
            
            else{
                st.push(s[i]);
            }
            
        }
        
        return ans;
        
    }
};