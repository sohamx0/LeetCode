/*
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

*/



class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = -1 , last = -1;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == target) {
                first = i;
                break;
            }
            
        }
        for(int i = nums.size() - 1; i >= 0; i--) {
            if(nums[i] == target) {
                last = i;
                break;
            }
            
        }
        return {first, last};
    }
};


/*
time complexity: O(n)
space complexity: O(1)
*/