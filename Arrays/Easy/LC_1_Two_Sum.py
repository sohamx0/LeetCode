# Problem: https://leetcode.com/problems/two-sum/
# Approach: Brute-force check all pairs and collect indices of a valid pair.
# This mirrors the straightforward nested-loop solution.
# Time: O(n^2) | Space: O(1)

# TWO SUM 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        L = [] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j :
                    continue
                elif nums[i] + nums[j] == target:
                    L.append(i)
                    L.append(j)
        a = len(L)/2
        L = L[:2]
        return L
    
print(Solution().twoSum([3,2,4], 6))
