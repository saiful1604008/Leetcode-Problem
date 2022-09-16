class Solution {
public:
    int firstUniqChar(string s) {
        map<char,int>m;
    for(int i=0;i<s.size();i++){
        m[s[i]]++;
    }
    //int flag=1;
    int idx;
    string ch;
    vector <string> res;
    for(int i=0;i<s.size();i++){
        if(m[s[i]]==1){
            //cout<< i << " " << s[i];
            return i;
            //ch = s[i];
            //flag=0;
            break;
        }
    }
            return - 1;
        
    }
};