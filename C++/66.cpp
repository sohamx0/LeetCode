/*
66. Plus One
Solved
Easy
Topics
premium lock icon
Companies
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
*/

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
    string s = "";
    vector<int> result;

    for (int i = 0; i < digits.size(); i++) {
        s += to_string(digits[i]);
    }

    long long num = stoll(s);
    num += 1;

    s = to_string(num);

    for (int i = 0; i < s.length(); i++) {
        result.push_back(s[i] - '0');
    }

    return result;
    }
};