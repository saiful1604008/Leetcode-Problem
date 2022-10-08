struct Node{
    Node *ar[26];
    bool flag;
};
class Trie {
public:
    Node* root;
    Trie() {
        root = new Node();
    }
    
    void insert(string word) {
        Node* n = root;
        for (int i = 0; i < word.length(); i++){
            if (n->ar[word[i] - 97] == NULL){
                n->ar[word[i] - 97] = new Node();
            }
            n = n->ar[word[i] - 97];
        }
        n->flag = true;
    }
    
    bool search(string word) {
        Node* n = root;
        for (int i = 0; i < word.length() && n != NULL; i++){
            if (n->ar[word[i] - 97] == NULL){
                return false;
            }
            n = n->ar[word[i] - 97];
        }
       return n->flag;
    }
    
    bool startsWith(string prefix) {
        Node* n = root;
        for (int i = 0; i < prefix.length() && n != NULL; i++){
            if (!n->ar[prefix[i] - 97]){
                return false;
            }
            n = n->ar[prefix[i] - 97];
        }
       return true;
        
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */