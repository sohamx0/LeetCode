/*
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

*/


class Solution {
public:
    string reverseWords(string s) {
        vector<string> arr;
        string word = "";
        string rev = "";
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != ' ') {
                word += s[i];
            } 
            else if (!word.empty()) {           // Needed help at this part, as i was confused in skipping the spaces and pushing the words in the vector
                arr.push_back(word);
                word = "";
            }
        }
        if (!word.empty()) {
            arr.push_back(word);
        }
        for (int j = arr.size() - 1; j >= 0; j--) {
            rev += arr[j];
            if (j > 0) {
                rev += " ";
            }
        }
        return rev;
    }
};