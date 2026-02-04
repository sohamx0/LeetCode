# Problem: https://leetcode.com/problems/maximum-number-of-bottles-you-can-drink/
# Approach: Simulate drinking and exchanges while the exchange cost increases.
# Track total drinks and empty bottles in a loop.
# Time: O(k) | Space: O(1)

# 3100. Maximum Number of Bottles You Can Drink


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        empty = numBottles
        while empty >= numExchange:
            # Only one exchange per value of numExchange
            empty -= numExchange
            drink += 1
            empty += 1
            numExchange += 1
        return drink
    

print(Solution().maxBottlesDrunk(9, 3))
