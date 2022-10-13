/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* Node = new TreeNode();
        
        if (root == NULL) return root;
        if (val < root->val) Node = searchBST(root->left, val);
        else if (val > root->val) Node = searchBST(root->right,val);
        else Node = root;
        
        return Node;
    }
};