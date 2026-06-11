/*
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
*/


class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        vector<int> x;
        int num = 1;
        int z = 0;

        while(x.size() < k) {
        if (z < arr.size() && arr[z] == num) {
            z++;
        } else {
            x.push_back(num);
        }
        num++;
    }
    return x[k - 1];
    }
};



// Solution is not optimal, but it works. We can optimize it by using binary search.
