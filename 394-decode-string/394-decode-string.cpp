class Solution {
public:
    string decodeString(string s) {
        stack <char> st;
        for (int i = 0; i < s.length(); i++){
            if(s[i] != ']'){
                st.push(s[i]);   
            }
            else{
                string temp = "";
                while (!st.empty() && st.top() != '['){
                    temp = st.top() + temp;
                    st.pop();
                }
                st.pop();
                
                string num = "";
                while(!st.empty() && isdigit(st.top())){
                    num = st.top() + num;
                    st.pop();
                }
                
                int k;
                k = stoi(num);
                
                while(k--){
                    for (char c:temp){
                        st.push(c);
                    }
                }
            }
        }
        
        string res = "";
        while (!st.empty()){
            res += st.top() ;
            st.pop();
        }
        
        reverse(res.begin(), res.end());
        return res;
        
    }
};