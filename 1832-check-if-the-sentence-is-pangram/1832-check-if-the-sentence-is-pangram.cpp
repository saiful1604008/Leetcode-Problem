class Solution {
public:
    bool checkIfPangram(string sentence) {
        vector <bool> mark(26, false);
        int index;
        
        for (int i = 0; i < sentence.size(); i++){
            if ('A' <= sentence[i] && 'Z' >= sentence[i]){
                index = sentence[i] - 'A';
            }
            else if ('a' <= sentence[i] && 'z' >= sentence[i]){
                index = sentence[i] - 'a';
            }
            else
                continue;
            
            mark[index] = true ;
            
        }
        for (int i= 0; i < 26; i++){
            if (mark[i] == false){
                return false;
            }
        
        }
        return true ;
        
    }
};