/*
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.
*/




class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int big = 0;
        for (int i = 0; i < s.size(); i++) {
            for (int j = i; j < s.size(); j++) {
                bool duplicate = false;
                for (int k = i; k < j; k++) {
                    if (s[k] == s[j]) {
                        duplicate = true;
                        break;
                    }
                }

                if (duplicate) {
                    break;
                }

                big = max(big, j - i + 1);
            }
        }

        return big;
    }
};

// Brute force Solution 