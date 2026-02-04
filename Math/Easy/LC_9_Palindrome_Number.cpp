// Problem: https://leetcode.com/problems/palindrome-number/
// Approach: Convert the number to a string and compare symmetric characters.
// Time: O(n) | Space: O(n)

// 9. Palindrome Number
/*
Given an integer x, return true if x is a palindrome, and false otherwise.
*/


class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        string s = to_string(x);
        int i = 0, j = s.size() - 1;
        while (i < j) {
            if (s[i] != s[j]) {
                return false;
            }
            i++; j--;
        }
        return true;
    }
};
