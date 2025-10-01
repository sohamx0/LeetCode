// LeetCode 1518. Water Bottles
// Given numBottles full water bottles, you can exchange numExchange empty bottles for one full bottle.
// Return the maximum number of water bottles you can drink.

class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int total = numBottles;  // total bottles you can drink
        while (numBottles >= numExchange) {
            int exchanged = numBottles / numExchange;  // how many new bottles you get
            total += exchanged;
            numBottles = exchanged + (numBottles % numExchange); // new full + leftover empty
        }
        return total;
    }
};