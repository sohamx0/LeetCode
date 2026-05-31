/*
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

*/

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int plant = 0;
        for (int i = 0; i < flowerbed.size(); i++) {
            bool left = (i == 0 || flowerbed[i-1] == 0); // for edge cases when i is 0, there is no left plot and when the left flowerbed is empty left is considered true
            bool right = (i == flowerbed.size()-1 || flowerbed[i+1] == 0); // for edge cases when i is at the last position, there is no right plot and when the right flowerbed is empty right is considered true
            if (flowerbed[i] == 0 && left && right) {
                flowerbed[i] = 1;
                plant++;
            }
        }
        return plant >= n;
    }
};
