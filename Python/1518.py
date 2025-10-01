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