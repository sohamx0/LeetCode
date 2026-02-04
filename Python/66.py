'''
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''




class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        new = []
        for i in range(len(digits)):
            s += str(digits[i])
        s = int(s)
        s += 1
        s = str(s)
        for i in range(len(s)):
            new.append(int(s[i]))

        return new