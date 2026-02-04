# Problem: https://leetcode.com/problems/sqrtx/
# Approach: Incrementally test squares until passing the target.
# Return the last integer whose square is not greater than x.
# Time: O(\sqrt{x}) | Space: O(1)

# 69. Sqrt(x)


class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i * i <= x:
            i += 1
        return i - 1

Solution().mySqrt(8)
