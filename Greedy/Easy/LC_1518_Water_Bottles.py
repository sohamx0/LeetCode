# Problem: https://leetcode.com/problems/water-bottles/
# Approach: Simulate exchanges while enough empty bottles exist to trade.
# Accumulate total bottles consumed during the process.
# Time: O(k) | Space: O(1)

# Water Bottles 

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        k = 0
        z = numBottles
        while numBottles >= numExchange:
            a = numBottles // numExchange
            k = k + a
            numBottles = a + (numBottles % numExchange)
        z = z + k 
        return z
    
print(Solution().numWaterBottles(15, 4))
