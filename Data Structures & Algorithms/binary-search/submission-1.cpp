class Solution {
public:
    int search(vector<int>& nums, int target) {
        int first = 0, last = nums.size()-1;
        int mid; 
        while (first <= last){
            mid = (first + last) / 2; 

            if (nums[mid] == target)
                return mid; 
            else if (nums[mid] > target)
                last = mid - 1; 
            else if (nums[mid] < target)
                first = mid +1; 
             
        }

        return -1;
    }
};
