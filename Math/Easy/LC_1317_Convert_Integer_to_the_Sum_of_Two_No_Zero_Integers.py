# Problem: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
# Approach: Try pairs (a, b) by incrementing a and decrementing b until both have no zero digits.
# This simple linear search satisfies the constraints.
# Time: O(n * d) | Space: O(1)

'''
1317. Convert Integer to the Sum of Two No-Zero Integers

No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.
'''



class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        a, b = 1, n - 1
        while "0" in str(a) or "0" in str(b):
            a += 1
            b -= 1
        return [a, b]
