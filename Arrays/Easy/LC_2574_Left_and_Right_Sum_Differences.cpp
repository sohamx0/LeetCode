/*
2574. Left and Right Sum Differences

You are given a 0-indexed integer array nums of size n.

Define two arrays leftSum and rightSum where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
*/




class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> leftSum;
        vector<int> rightSum;
        vector<int> answer;
        leftSum.push_back(0);
        rightSum.push_back(0);
        for(int i = 1; i < nums.size(); i++) {
            leftSum.push_back(leftSum[i - 1] + nums[i - 1]);
        }
        for(int j = nums.size() - 2; j >= 0; j--) {
            rightSum.push_back(rightSum[nums.size() - 2 - j] + nums[j + 1]);
        }
        for(int k = 0; k < nums.size(); k++) {
            answer.push_back(abs(leftSum[k] - rightSum[nums.size() - 1 - k]));
        }
        return answer;
    }
};


