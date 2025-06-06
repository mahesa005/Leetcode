class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        int lastIdx = nums.size() - 1;
        for (int i = 0; i <= lastIdx; i++) {
            if (nums[i] != val) {
                k++;
            }
            else {
                for (int j = lastIdx; j > i; j--) {
                    if (nums[j] != val) {
                        swap(nums[i], nums[j]);
                        k++;
                        lastIdx--;
                        break; 
                    }
                }
            }
        }
        return k;
    }
};