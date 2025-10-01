# SINGLE NUMBER

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''


class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:                                                            # Time: O(n)
            result ^= num                                                           
        return result
    """ 
How does this work :
The XOR operation has a few key properties that make it useful for this problem:
1. a ^ a = 0 (XORing a number with itself gives 0)
2. a ^ 0 = a (XORing a number with 0 gives the number itself)
3. XOR is commutative and associative (the order of operations doesn't matter)

Using these properties, we can XOR all the numbers in the array. Pairs of identical numbers will cancel each other out (because of property 1), and the only number that doesn't get canceled out is the single number we're looking for.

"""

    def singleNumber2(self, nums):
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):                                                  # Time: O(n^2)
            unique = True                                                           
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    unique = False
                    break
            if unique:
                return nums[i]
            
print(Solution().singleNumber2([4,1,2,1,2]))