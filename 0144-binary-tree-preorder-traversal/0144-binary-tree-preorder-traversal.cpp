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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) {
            return res;
        }
        else {
            res.push_back(root->val);
            vector<int> left = preorderTraversal(root->left);
            for (int i = 0; i < left.size(); i++) {
                res.push_back(left[i]);
            }
             vector<int> right = preorderTraversal(root->right);
            for (int i = 0; i < right.size(); i++) {
                res.push_back(right[i]);
            }
        }
        return res;
    }
};