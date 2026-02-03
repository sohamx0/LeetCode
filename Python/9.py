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