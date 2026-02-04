# Problem: https://leetcode.com/problems/palindrome-number/
# Approach: Convert to string and compare with its reverse.
# This directly checks palindrome symmetry.
# Time: O(n) | Space: O(n)

'''
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
'''




class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        List = x[::]
        if x[::]==x[::-1]:
            return True
        else:
            return False

Solution().isPalindrome(167)
