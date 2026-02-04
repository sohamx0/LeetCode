# Problem: https://leetcode.com/problems/self-dividing-numbers/
# Approach: For each number in range, check that all digits divide it and none are zero.
# Collect numbers that satisfy the condition.
# Time: O(n * d) | Space: O(1)

'''
728. Self Dividing Numbers
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

'''




class Solution(object):
    def selfDividingNumbers(self, left, right):
        final = []                  # List to store self-dividing numbers
        count = 0
        for i in range(left,right+1):
            for j in range(len(str(i))):
                l = list(str(i))
                if int(l[j]) == 0:
                    break
                if i % int(l[j]) == 0:
                    count += 1
            if count == len(str(i)):
                final.append(i)
            count = 0

        return final
